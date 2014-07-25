import os
from pyrrd.graph import Graph, LINE, DEF, CDEF, AREA

def draw(rrd_file_name, img_file_name, start_time, end_time):
    rrd_file_name = '/tmp/mem.rrd'
    mem_total = os.popen("free -b | head -2 | tail -1 | awk '{print $2}'").read()
    data_mem_used = DEF(vname='used', rrdfile=rrd_file_name, dsName='mem_used')
    #data_mem_free = DEF(vname='free', rrdfile=rrd_file_name, dsName='mem_free')
    data_mem_buffers = DEF(vname='buffers', rrdfile=rrd_file_name, dsName='mem_buffers')
    data_mem_cached = DEF(vname='cached', rrdfile=rrd_file_name, dsName='mem_cached')
    data_mem_buffers_and_cached_over_used = CDEF(vname='bacou', rpn='buffers,cached,+')
    data_mem_real_used = CDEF(vname='real_used', rpn='used,bacou,-')

    line_total = LINE(value=int(mem_total), color='#000000', legend='Total')
    area_used = AREA(defObj=data_mem_real_used, color='#FF0000', legend='Used')
    area_buffers_and_cached = AREA(defObj=data_mem_buffers_and_cached_over_used, color='#0000FF', legend='Buffers And Cached Over Used', stack=True)
    img = Graph(filename=img_file_name, title='Memory\ Infomation', start=start_time, end=end_time, base=1024)
    img.data.extend([data_mem_used, data_mem_buffers, data_mem_cached, data_mem_buffers_and_cached_over_used,data_mem_real_used, line_total, area_used, area_buffers_and_cached])
    img.write()

if __name__ == '__main__':
    pass


#end_time = int(time.time())
#start_time = end_time - 60
#if len(sys.argv) > 1:
#    if sys.argv[1] == '1m':
#        start_time = end_time - 60
#    elif sys.argv[1] == '1h':
#        start_time = end_time - 3600
#    elif sys.argv[1] == '1d':
#        start_time = end_time - 86400







