# This python script collects metrics about linux server. 
#### 1) Python script usage examples:

OS release: 
```
./metrics os
System: Linux
Platform: 3.10.0-1127.13.1.el7.x86_64
machine: x86_64
```
CPU frequency and metrics:
```
./metrics cpu
CPU frequency current: 2381.679833333333 MHz
Number of cores in system: 12
Number of physical cores in system: 6
Number of logical cores in system: 12
system.cpu.user: 965.59
system.cpu.system: 257.64
system.cpu.idle: 34391.71
system.cpu.nice: 8.17
system.cpu.iowait: 12.14
system.cpu.irq: 84.03
system.cpu.softirq: 30.42
system.cpu.steal: 0.0
system.cpu.guest: 0.0
```
Disk usage:
```
./metrics disk
total 24.99 GB /
used 3.97 GB /
free 21.02 GB /
percent of disk_usage: 15.9 % /
```
Memory metrics:
```
./metrics memory
virtual total: 15.42 GB
virtual available: 11.12 GB
virtual used: 3.37 GB
virtual free: 8.12 GB
virtual active: 1.90 GB
virtual inactive: 4.37 GB
virtual buffers: 0.15 GB
virtual cached: 3.78 GB
virtual shared: 0.62 GB
```
Uptime:
```
./metrics uptime
System boot time: 2020-07-02 19:59:46
```
Swap usage:
```
./metrics swap
swap total: 12641624064
swap used: 0
swap free: 12641624064
swap percent: 0.0
swap sin: 0
swap sout: 0
```
Processes:
```
$ ./metrics processes | head -10
PID | ProcessName | Username
1 | systemd | root
2 | kthreadd | root
3 | rcu_gp | root
4 | rcu_par_gp | root
6 | kworker/0:0H-kblockd | root
9 | mm_percpu_wq | root
10 | ksoftirqd/0 | root
11 | rcu_sched | root
12 | migration/0 | root
```
#### 2) Docker image usage examples:
 * It displays information about processes running on the host machine from within the container environment. 
 * It displays usernames for processes running on the host machine from within the container environment. 
```
$ ls
Dockerfile  metrics  README.md
$ docker build -t metrics_img .
$ docker run -it --pid=host -v /etc/passwd:/etc/passwd:ro metrics_img metrics processes |grep -v root |head -5
PID | ProcessName | Username
937 | systemd-resolved | systemd-resolve
960 | dbus-broker-launch | dbus
961 | dbus-broker | dbus
965 | avahi-daemon | avahi
```
