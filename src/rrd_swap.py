from pyrrd.rrd import RRD, RRA, DataSource
import os, time

def define(rrd_file_name):
    data_sources = []
    data_sources.append(DataSource(dsName='swap_used', dsType='GAUGE', heartbeat=10))

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
    start_time = int(time.time())
    swap_rrd= RRD(filename=rrd_file_name, start=start_time, step=1, ds=data_sources, rra=rras)
    return swap_rrd

def create(rrd_file_name, swap_rrd, new):
    if new:
        swap_rrd.create()
    elif not os.path.isfile(rrd_file_name):
        swap_rrd.create()

def run(rrd_file_name, new):
    mem_rrd = define(rrd_file_name)
    create(rrd_file_name, mem_rrd, new)
    while True:
        time.sleep(1)
        swap_used = os.popen("free -b | tail -1 | awk '{print $3}'").read()
        mem_rrd.bufferValue(time.time().__trunc__(), swap_used)
        mem_rrd.update(template='swap_used')

if __name__ == '__main__':
    rrd_file_name = '/tmp/swap.rrd'
    run(rrd_file_name, False)
