#!/bin/env python
# cat /proc/net/dev | head -3 | tail -1 | awk '{print $2, $10}'
# This program can save the network rx tx speed in rrdtool.
# You can print the image using rrdtool_graph.
from pyrrd.rrd import RRD, RRA, DataSource
import os
import time

def define(rrd_file_name):
    data_sources = []
    data_sources.append(DataSource(dsName='eth0_rx', dsType='COUNTER', heartbeat=10))
    data_sources.append(DataSource(dsName='eth0_tx', dsType='COUNTER', heartbeat=10))
    rras = []
    # 1 * 1 * 300 = 300s = 5min
    rras.append(RRA(cf='AVERAGE', xff='0.5', steps=1, rows=300))
    # 1 * 5 * 720 = 3600s = 1h
    rras.append(RRA(cf='AVERAGE', xff='0.5', steps=5, rows=720))
    # 1 * 10 * 8640 = 86400 = 1day
    rras.append(RRA(cf='AVERAGE', xff='0.5', steps=10, rows=8640))
    # 1 * 60 * 10080 = 7day = 1week
    rras.append(RRA(cf='AVERAGE', xff='0.5', steps=60, rows=10080))
    # 1 * 300 * 8928 = 31day = 1month
    rras.append(RRA(cf='AVERAGE', xff='0.5', steps=300, rows=8640))
    # 1 * 3660 * 8640 = 366day = 1year
    rras.append(RRA(cf='AVERAGE', xff='0.5', steps=3660, rows=8640))

    rrd_start_time = int(time.time())
    network_rrd = RRD(filename=rrd_file_name, start=rrd_start_time, ds=data_sources, rra=rras, step=1)
    return network_rrd

def create(rrd_file_name, network_rrd, new):
    if new:
        network_rrd.create()
    elif not os.path.isfile(rrd_file_name):
        network_rrd.create()

def run(rrd_file_name, new):
    network_rrd = define(rrd_file_name)
    create(rrd_file_name, network_rrd, new)
    while True:
        time.sleep(1)
        ifstat_rx_tx_bytes = os.popen("cat /proc/net/dev | head -3 | tail -1 | awk '{print $2, $10}'")
        rx_bytes, tx_bytes = ifstat_rx_tx_bytes.read().split(' ')
        network_rrd.bufferValue(str(time.time().__trunc__()), rx_bytes, tx_bytes)
        network_rrd.update(template='eth0_rx:eth0_tx')

if __name__ == '__main__':
    rrd_file_name = '/tmp/ifstat.rrd'
    run(rrd_file_name, False)

