#!/bin/env python
#command: free | head -2 | tail -1 | awk '{print $2, $3, $4, $6, $7}'
from pyrrd.rrd import RRD, RRA, DataSource
import os, time

def define(rrd_file_name):
    data_sources = []
    data_sources.append(DataSource(dsName='mem_used', dsType='GAUGE', heartbeat=10))
    data_sources.append(DataSource(dsName='mem_free', dsType='GAUGE', heartbeat=10))
    data_sources.append(DataSource(dsName='mem_buffers', dsType='GAUGE', heartbeat=10))
    data_sources.append(DataSource(dsName='mem_cached', dsType='GAUGE', heartbeat=10))

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
    rrd_file_name = '/tmp/mem.rrd'
    start_time = int(time.time())
    mem_rrd = RRD(filename=rrd_file_name, start=start_time, step=1, ds=data_sources, rra=rras)
    return mem_rrd

def create(rrd_file_name, mem_rrd, new):
    if new:
        mem_rrd.create()
    elif not os.path.isfile(rrd_file_name):
        mem_rrd.create()

def run(rrd_file_name, new):
    mem_rrd = define(rrd_file_name)
    create(rrd_file_name, mem_rrd, new)
    while True:
        time.sleep(1)
        mem_used, mem_free, mem_buffers, mem_cached = os.popen("free -b | head -2 | tail -1 | awk '{print $3, $4, $6, $7}'").read().split(' ')
        mem_rrd.bufferValue(time.time().__trunc__(), mem_used, mem_free, mem_buffers, mem_cached)
        mem_rrd.update(template='mem_used:mem_free:mem_buffers:mem_cached')

if __name__ == '__main__':
    rrd_file_name = '/tmp/mem.rrd'
    run(rrd_file_name, False)

