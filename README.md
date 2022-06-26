# tcp-ping
A simple Pyhton script to check connection perfomance via TCP protocol for hosts that do not allow ICMP

It is a simple script inspired by yantisj tcpping script with some modules addes, like optparser and a summary of the perfomance measured.

# Installation
This script requires Python3.

Clone the repository.

```shell
$ git clone git@github.com:RichardsonOliveira/tcp-ping.git
```
Go to the folder where it is located.
```shell
$ cd tcp-ping
```

# Usage
Upon starting the script without any parameters, it will show the help message below:
```shell
Simple Script to check perfomance connection on hosts that do not allow ICMP
ping.

Options:
  -h, --help            show this help message and exit
  -H HOST, --host=HOST  Host addres to connect
  -P PORT, --port=PORT  TCP port to connect.
  -c MAXCOUNT, --maxcount=MAXCOUNT
                        Count of pings.
```

This script requires 3 parameters, Host (-H), Port (-P) and count (-c).
A simple commando to verify perfomance to google is:
```shell
$ python3 tcpping.py -H google.com -P 443 -c 10
```
The command above will perfom 10 pings to google.com address on port 443, and then show you the perfomance, as shown below.
```shell
[...]
Connected to google.com at Port 443 (HTTPS): tcp_seq=9 RTD = 4.19 ms

TCP Ping Results: Connections (Total/Passed/Failed): [10/10/0]

Latency Metrics: 

Minimun: 17.16 ms 
Average: 5.42 ms 
Maximum: 6.24 ms 
Packet Loss: 0%
```
