import os, time
from pyrrd.rrd import DataSource, RRD, RRA

def define(rrd_file_name):
    """
    define a cpu rrd file.
    :return cpu_rrd
    """
    data_sources = []
    data_sources.append(DataSource(dsName='total', dsType='COUNTER', heartbeat=10))
    data_sources.append(DataSource(dsName='user', dsType='COUNTER', heartbeat=10))
    data_sources.append(DataSource(dsName='system', dsType='COUNTER', heartbeat=10))
    data_sources.append(DataSource(dsName='nice', dsType='COUNTER', heartbeat=10))
    data_sources.append(DataSource(dsName='iowait', dsType='COUNTER', heartbeat=10))
    data_sources.append(DataSource(dsName='irq', dsType='COUNTER', heartbeat=10))
    data_sources.append(DataSource(dsName='softirq', dsType='COUNTER', heartbeat=10))
    data_sources.append(DataSource(dsName='idle', dsType='COUNTER', heartbeat=10))
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
    cpu_rrd = RRD(filename=rrd_file_name, start=start_time, step=1, ds=data_sources, rra=rras)
    return cpu_rrd

def create(rrd_file_name, cpu_rrd, new):
    if new:
        cpu_rrd.create()
    elif not os.path.isfile(rrd_file_name):
        cpu_rrd.create()

def run(rrd_file_name, new):
    cpu_rrd = define(rrd_file_name)
    create(rrd_file_name, cpu_rrd, new)
    while True:
        time.sleep(1)
        f = os.popen("cat /proc/stat | head -1 | awk '{print $2,$3,$4,$5,$6,$7,$8}'").read()
        total = str(reduce(lambda x, y: x + y, map(int, f.split(' '))))
        user, nice, system, idle, iowait, irq, softirq = f.split(' ')
        #print total, user, nice, system, idle, iowait, irq, softirq
        cpu_rrd.bufferValue(time.time().__trunc__(), total, user, nice, system, idle, iowait, irq, softirq)
        cpu_rrd.update(template='total:user:nice:system:idle:iowait:irq:softirq')

if __name__ == '__main__':
    rrd_file_name = '/tmp/cpu.rrd'
    run(rrd_file_name, False)

