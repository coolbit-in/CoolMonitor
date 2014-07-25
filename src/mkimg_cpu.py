from pyrrd.graph import Graph, LINE, AREA, DEF, CDEF

def draw(rrd_file_name, img_file_name, start_time, end_time):
    data_total = DEF(vname='data_total', rrdfile=rrd_file_name, dsName='total')
    data_user = DEF(vname='data_user', rrdfile=rrd_file_name, dsName='user')
    data_nice = DEF(vname='data_nice', rrdfile=rrd_file_name, dsName='nice')
    data_system = DEF(vname='data_system', rrdfile=rrd_file_name, dsName='system')
    data_iowait = DEF(vname='data_iowait', rrdfile=rrd_file_name, dsName='iowait')
    data_idle = DEF(vname='data_idle', rrdfile=rrd_file_name, dsName='idle')
    data_irq = DEF(vname='data_irq', rrdfile=rrd_file_name, dsName='irq')
    data_softirq= DEF(vname='data_softirq', rrdfile=rrd_file_name, dsName='softirq')
    cdata_irq_add_softirq = CDEF('cdata_irq_and_softirq', rpn='data_irq,data_softirq,+,data_total,/,100,*')
    cdata_user_add_nice = CDEF('cdata_user_and_nice', rpn='data_user,data_nice,+,data_total,/,100,*')
    cdata_system = CDEF('cdata_system', rpn='data_system,data_total,/,100,*')
    cdata_iowait= CDEF('cdata_iowait', rpn='data_iowait,data_total,/,100,*')

    line_total = LINE(value=100, color='#000000')
    area_system = AREA(defObj=cdata_system, color='#FF0000', legend='System', stack=True)
    area_user= AREA(defObj=cdata_user_add_nice, color='#0000FF', legend='User', stack=True)
    area_iowait= AREA(defObj=cdata_iowait, color='#00FF00', legend='IO', stack=True)
    area_irq= AREA(defObj=cdata_irq_add_softirq, color='#FFFF00', legend='IRQ', stack=True)
    img = Graph(filename='img_file_name', start=start_time, end=end_time, title='cpu\ load')
    img.data.extend([data_total, data_user, data_nice, data_system, data_iowait, data_irq, data_softirq, cdata_system, cdata_user_add_nice, cdata_iowait, cdata_irq_add_softirq,area_system, area_user, area_iowait, area_irq, line_total])
    img.write()

if __name__ == '__main__':
    pass
#        start_time = end_time - 60
#    if sys.argv[1] == '1m':
#        start_time = end_time - 60
#    elif sys.argv[1] == '1h':
#        start_time = end_time - 3600
#    elif sys.argv[1] == '1d':
#        start_time = end_time - 86400


