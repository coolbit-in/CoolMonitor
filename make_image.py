from src import mkimg_cpu, mkimg_memory, mkimg_network
import argparse
import time


def check_time():
    if args.block is None:
        #TODO check -e -s
        pass
    else:
        num, unit = args.block.split(':')
        num = int(num)
        time_block = 0
        if unit == 'S':
            time_block = num
        elif unit == 'M':
            time_block = num * 60
        elif unit == 'H':
            time_block = num * 60 * 60
        elif unit == 'D':
            time_block = num * 60 * 60 * 24
        else:
            #TODO Error Exception
            pass
        end_time = int(time.time())
        start_time = end_time - time_block
    return start_time, end_time

if __name__ == '__main__':
    args_parser = argparse.ArgumentParser()
    group = args_parser.add_mutually_exclusive_group()
    group.add_argument('-c', '--cpu', help='', action='store_true')
    group.add_argument('-m', '--memory', help='', action='store_true')
    group.add_argument('-n', '--network', help='', action='store_true')
    args_parser.add_argument('rrd_file_name', help='')
    args_parser.add_argument('img_file_name', help='')
    args_parser.add_argument('-s','--start', help='[year/mon/day/hour/min/sec]')
    args_parser.add_argument('-e','--end', help='[year/mon/day/hour/min/sec]')
    args_parser.add_argument('-b', '--block', help='[n:S|M|H|D]')
    args = args_parser.parse_args()

    start_time, end_time = check_time()
    if args.cpu:
        mkimg_cpu.draw(args.rrd_file_name, args.img_file_name, start_time, end_time)
    elif args.memory:
        mkimg_memory.draw(args.rrd_file_name, args.img_file_name, start_time, end_time)
    elif args.network:
        mkimg_network.draw(args.rrd_file_name, args.img_file_name, start_time, end_time)

