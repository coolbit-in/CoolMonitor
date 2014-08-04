import os
from pyrrd.graph import Graph, LINE, DEF, CDEF, AREA

def draw(rrd_file_name, img_file_name, start_time, end_time):
    swap_total = os.popen("free -b | tail -1 | awk '{print $2}'").read()
    data_swap_used = DEF(vname='used', rrdfile=rrd_file_name, dsName='swap_used')

    line_total = LINE(value=int(swap_total), color='#000000', legend='Total')
    area_used = AREA(defObj=data_swap_used, color='#FF0000', legend='Used')
    img = Graph(filename=img_file_name, title='Swap\ Infomation', start=start_time, end=end_time, base=1024)
    img.data.extend([data_swap_used, line_total, area_used])
    img.write()

if __name__ == '__main__':
    pass
