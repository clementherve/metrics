# This python script collects metrics about linux server. 
Script usage examples:

### OS release: ###
```
./metrics os
System: Linux
Platform: 3.10.0-1127.13.1.el7.x86_64
machine: x86_64
```
### CPU metrics: ###
```
./metrics cpu
Number of cores in system: 1
Number of physical cores in system: 1
Number of logical cores in system: 1
system.cpu.user: 16574.05
system.cpu.system: 12777.58
system.cpu.idle: 14559397.14
system.cpu.nice: 394.84
system.cpu.iowait: 545.74
system.cpu.irq: 0.0
system.cpu.softirq: 111.35
system.cpu.steal: 930.16
system.cpu.guest: 0.0
```

### Memory metrics: ###
```
./metrics memory
virtual total: 1927180288
virtual available: 1351569408
virtual used: 274817024
virtual free: 441622528
virtual active: 679624704
virtual inactive: 572559360
virtual buffers: 0
virtual cached: 1210740736
virtual shared: 117174272
```
### Uptime: ###
```
./metrics uptime
System boot time: 2020-07-02 19:59:46
```

### Disk usage: ###
```
./metrics disk
disk_usage for / total: 26831990784
disk_usage for / used: 4264550400
disk_usage for / free: 22567440384
disk_usage for / percent: 15.9 %
```
