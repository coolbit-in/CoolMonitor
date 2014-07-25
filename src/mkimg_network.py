from pyrrd.graph import Graph, DEF, LINE
def draw(rrd_file_name, img_file_name, start_time, end_time):
    data_rx= DEF(vname='rx', rrdfile=rrd_file_name, dsName='eth0_rx')
    data_tx= DEF(vname='tx', rrdfile=rrd_file_name, dsName='eth0_tx')

    graph_line_rx = LINE(defObj=data_rx, color='#FF0000', legend='rx speed')
    graph_line_tx = LINE(defObj=data_tx, color='#0000FF', legend='tx speed')
    img = Graph(filename=img_file_name, start=start_time, end=end_time, title='rx\ speed\ img', base=1024)
    img.data.extend([data_rx, data_tx, graph_line_rx, graph_line_tx])
    img.write()

if __name__ == '__main__':
    pass
