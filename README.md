# This python script collects metrics about linux server. 
Script usage examples:

#### OS release: 
```
./metrics os
System: Linux
Platform: 3.10.0-1127.13.1.el7.x86_64
machine: x86_64
```
#### CPU frequency and metrics:
```
./metrics cpu
CPU frequency current: 2499.998 MHz
Number of cores in system: 1
Number of physical cores in system: 1
Number of logical cores in system: 1
system.cpu.user: 16702.86
system.cpu.system: 12892.77
system.cpu.idle: 14647792.72
system.cpu.nice: 397.72
system.cpu.iowait: 546.15
system.cpu.irq: 0.0
system.cpu.softirq: 112.07
system.cpu.steal: 936.76
system.cpu.guest: 0.0
```
#### Disk usage:
```
./metrics disk
total 24.99 GB /
used 3.97 GB /
free 21.02 GB /
percent of disk_usage: 15.9 % /
```
#### Memory metrics:
```
./metrics memory
virtual total: 1.79 GB
virtual available: 1.27 GB
virtual used: 0.24 GB
virtual free: 0.42 GB
virtual active: 0.63 GB
virtual inactive: 0.53 GB
virtual buffers: 0.00 GB
virtual cached: 1.13 GB
virtual shared: 0.11 GB
```
#### Uptime:
```
./metrics uptime
System boot time: 2020-07-02 19:59:46
```
#### Swap usage:
```
./metrics swap
swap total: 0
swap used: 0
swap free: 0
swap percent: 0.0
swap sin: 0
swap sout: 0
```
