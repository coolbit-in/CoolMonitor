from bottle import route, run, template, request, static_file
import os
@route('/')
def index():
    return template('index')


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filename=filepath, root='views/static')

@route('/api')
def api():
    rq_type= request.query.type
    time_b = request.query.b
    time_unit = request.query.unit
    rrd_file_name = {'c': 'cpu.rrd', 'm': 'mem.rrd', 'n': 'net.rrd'}[rq_type]
    img_file_name = {'c': 'cpu.png', 'm': 'mem.png', 'n': 'net.png'}[rq_type]
    rrd_file_root = '/home/coolbit/computer/python/project_cool_monitor/tmp'
    img_file_root = 'cache'
    script_path = '/home/coolbit/computer/python/project_cool_monitor/make_image.py'
    command_line = 'python {script_path} -{rq_type} -b {time_b}:{time_unit} {rrd_file_root}/{rrd_file_name} {img_file_root}/{img_file_name}'.format(script_path=script_path, rq_type=rq_type, time_b=time_b, time_unit=time_unit, rrd_file_root=rrd_file_root, rrd_file_name=rrd_file_name, img_file_root=img_file_root, img_file_name=img_file_name)
    os.popen(command_line)
    return static_file(filename=img_file_name, root=img_file_root, mimetype='image/png')

run(host='127.0.0.1', port='9001', debug=True)