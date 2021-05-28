#!/usr/bin/python3
# -*- coding: utf-8 -*-
import psutil
import datetime
import platform
import json
from http.server import BaseHTTPRequestHandler, HTTPServer



def os():
    data = {
        'system': platform.system(),
        'platform': platform.release(),
        'machine': platform.machine()
    }
    return data



def uptime():
    data = {'uptime': datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")}
    return data



def disk():
    du = psutil.disk_usage('/')
    disk_usage_total = du.total
    disk_usage_used = du.used
    disk_usage_free = du.free
    data = {
        'total': str(round(disk_usage_total / (1024.0 ** 3))) + " Gb",
        'used': str(round(disk_usage_used / (1024.0 ** 3))) + " Gb",
        'free': str(round(disk_usage_free / (1024.0 ** 3))) + " Gb",
        'percent': psutil.disk_usage('/').percent
    }
    return data



def cpu():
    data = {
        'current_freq': str(round(psutil.cpu_freq().current)) + ' MHz',
        'cores': psutil.cpu_count(),
        'physical_cores': psutil.cpu_count(logical=False),
        'logical_cores': psutil.cpu_count(logical=True),
        'users': psutil.cpu_times().user,
        'system': psutil.cpu_times().system,
        'idle': psutil.cpu_times().idle,
        'nice': psutil.cpu_times().nice,
        'iowait': psutil.cpu_times().iowait,
        'irq': psutil.cpu_times().irq,
        'softirq': psutil.cpu_times().softirq,
        'steal': psutil.cpu_times().steal,
        'guest': psutil.cpu_times().guest
    }
    return data



def memory():
    vm = psutil.virtual_memory()
    data = {
        'virtual_total': str(round(vm.total / (1024.0 ** 3))) + " Gb",
        'virtual_avail':str(round(vm.available / (1024.0 ** 3))) + " Gb",
        'virtual_used': str(round(vm.used / (1024.0 ** 3))) + " Gb",
        'virtual_free': str(round(vm.free / (1024.0 ** 3))) + " Gb",
        'virtual_active': str(round(vm.active / (1024.0 ** 3))) + " Gb",
        'virtual_inactive': str(round(vm.inactive / (1024.0 ** 3))) + " Gb",
        'virtual_buffers': str(round(vm.buffers / (1024.0 ** 3))) + " Gb",
        'virtual_cached': str(round(vm.cached / (1024.0 ** 3))) + " Gb",
        'virtual_shared': str(round(vm.shared / (1024.0 ** 3))) + " Gb",
    }
    return data



def swap():
    sw = psutil.swap_memory()
    data = {
        'total': str(round(sw.total / (1024.0 ** 3))) + " Gb",
        'used': str(round(psutil.swap_memory().used / (1024.0 ** 3))) + " Gb",
        'free': str(round(psutil.swap_memory().free / (1024.0 ** 3))) + " Gb",
        'percent': str(round(psutil.swap_memory().percent / (1024.0 ** 3))) + " Gb",
        'swap_in': str(round(psutil.swap_memory().sin / (1024.0 ** 3))) + " Gb",
        'swap_out': str(round(psutil.swap_memory().sout / (1024.0 ** 3))) + " Gb",
    }
    return data



def processes():
    data = []
    curProcesses = psutil.process_iter()
    for eachProcess in curProcesses:
        data.append({
            'pid': eachProcess.pid,
            'name': eachProcess.name(),
            'user': eachProcess.username()
        })
    return data



class ExporterServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/metrics":
            data = {
                "os": os(),
                "uptime": uptime(),
                "cpu": cpu(),
                "memory": memory(),
                "disk": disk(),
                "swap": swap()
            }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json.dumps(data), "utf-8"))



webServer = HTTPServer(("127.0.0.1", 8080), ExporterServer)
try:
    webServer.serve_forever()
except KeyboardInterrupt:
    webServer.server_close()


# swap()
# processes()
