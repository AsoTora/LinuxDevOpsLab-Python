#!/usr/bin/env python
# installed
import psutil

# default
import time
from psutil._common import bytes2human
import configparser
import json

time_format = "%Y-%m-%d-%H-%M"


class SystemInfo():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def CpuInfo(self):
        return str(psutil.cpu_percent()) + '%'

    def MemoryInfo(self):
        disks = psutil.disk_usage('/')
        virt = psutil.virtual_memory()
        swap = psutil.swap_memory()

        vmem = {'total': str(bytes2human(virt.total)),
                'used': str(bytes2human(virt.used)),
                'free': str(bytes2human(virt.free)), }

        swp = {'total': str(bytes2human(swap.total)),
               'used': str(bytes2human(swap.used)),
               'free': str(bytes2human(swap.free))}

        mem = {'total': str(bytes2human(disks.total)),
               'used': str(bytes2human(disks.used)),
               'free': str(bytes2human(disks.free))}

        return {'virtyal_memory': vmem, 'swap': swp, 'disk_usage': mem}

    def IOinfo(self):
        info = psutil.disk_io_counters()
        return {'Total disk READ': str(bytes2human(info.read_bytes)),
                'Total disk WRITE': str(bytes2human(info.write_bytes))}

    def NetworkInfo(self):
        info = psutil.net_io_counters(pernic=True)
        connections = list(info.keys())
        connections.sort(key=lambda x: sum(info[x]), reverse=True)

        net = {}
        for name in connections:
            stats = info[name]
            net[name] = {"bytes-sent": str(bytes2human(stats.bytes_sent)),
                         "bytes-recv": str(bytes2human(stats.bytes_recv)),
                         "pkts-sent": str(bytes2human(stats.packets_sent)),
                         "pkts-recv": str(bytes2human(stats.packets_recv))}
        return net

    def __str__(self):
        print(" *** CPU *** ")
        print(self.CpuInfo())

        print("")
        print("*** MEMORY *** ")
        print(self.MemoryInfo())

        print("")
        print("*** IO *** ")
        print(self.IOinfo())

        print("")
        print("*** NetWork *** ")
        print(self.NetworkInfo())

        return "****" * 100


def write_txt(count):
    data = SystemInfo()
    with open('data.txt', 'a') as f:
        f.write('\n' + 'SNAPSHOT ' + str(count) + ': ' + time.strftime(time_format) + ":\n")
        f.write('\t\t\t' + 'CPU: ' + str(data.CpuInfo()) + '\n')

        f.write('\t\t\t' + 'Memory:' + '\n')
        memory = data.MemoryInfo()
        for key in memory:
            f.write("{}{}:\n".format('\t' * 4, key))
            for k, v in memory[key].items():
                f.write("{}{}: {}\n".format('\t' * 5, k, v))

        f.write('\t\t\t' + 'IO:' + '\n')
        io = data.IOinfo()
        for key in io:
            f.write("{}{}: {}\n".format('\t' * 4, key, io[key]))

        f.write('\t\t\t' + 'NETWORK:' + '\n')
        net = data.NetworkInfo()
        for connect in net:
            f.write("{}{}:\n".format('\t' * 4, connect))
            for k, v in net[connect].items():
                f.write("{}{}: {}\n".format('\t' * 5, k, v))


def write_json(count, snaps):
    data = SystemInfo()
    snaps['SNAPSHOT ' + str(count) + ': ' + time.strftime(time_format)] = {
        'CPU': data.CpuInfo(),
        'Memory': data.MemoryInfo(),
        'IO': data.IOinfo(),
        'NETWORK': data.NetworkInfo()
    }
    with open('data.json', 'w') as f:
        json.dump(snaps, f, indent=2)


def config():
    params = {'output': 'txt', 'interval': '5'}  # default values
    config = configparser.ConfigParser()
    config.read('./config.ini')

    # read config file
    for sect in config.sections():
        for key in config[sect]:
            if key not in params.keys():
                continue
            params[key] = config[sect][key]
    return params


def run():
    params = config()
    c = 0
    interval = int(params['interval'])
    snaps = {}

    while True:
        if params['output'] == 'console':
            print('SNAPSHOT ' + str(c) + ': ' + time.strftime(time_format) + "\n")
            print(SystemInfo())

        elif params['output'] == 'txt':
            write_txt(c)

        elif params['output'] == 'json':
            write_json(c, snaps)

        else:
            print('Unsuported format')
            break

        c += 1
        time.sleep(60 * interval)
