#!/usr/bin/env python
from src import rrd_cpu, rrd_memory, rrd_network, rrd_swap
import argparse
import threading
args_parser = argparse.ArgumentParser()
args_parser.add_argument('-n', '--new', help='', action='store_true')
args_parser.add_argument('path', help='file path.', type=str)
args = args_parser.parse_args()

if args.path[-1] != '/':
    args.path = args.path + '/'
print args.path

cpu_rrd_file_name = args.path + 'cpu.rrd'
memory_rrd_file_name = args.path + 'mem.rrd'
network_rrd_file_name = args.path + 'net.rrd'
swap_rrd_file_name = args.path + 'swap.rrd'

def target_cpu():
    rrd_cpu.run(cpu_rrd_file_name, args.new)

def target_memory():
    rrd_memory.run(memory_rrd_file_name, args.new)

def target_network():
    rrd_network.run(network_rrd_file_name, args.new)
def target_swap():
    rrd_swap.run(swap_rrd_file_name, args.new)

threading.Thread(target=target_cpu).start()
threading.Thread(target=target_memory).start()
threading.Thread(target=target_network).start()
threading.Thread(target=target_swap()).start()


