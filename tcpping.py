#!/usr/bin/env python3

import optparse
import statistics
import sys
import socket
import time
import signal
from timeit import default_timer as timer

#Creating options for console command
def Main():
    p = optparse.OptionParser(description="Simple Script to check perfomance connection on hosts that do not allow ICMP ping.")
    p.add_option('-H', '--host', 
                action = 'store', 
                type = 'string', 
                dest = 'host', 
                default = None, 
                help = 'Host addres to connect')

    p.add_option('-P', '--port', 
                action = 'store', 
                type = 'int', 
                dest = 'port', 
                default = None, 
                help = 'TCP port to connect.')

    p.add_option('-c', '--maxcount',
                action = 'store',
                type = 'int',
                dest = 'maxCount',
                default = None,
                help = 'Count of pings.')

    (options, args) = p.parse_args()
    host = options.host
    port = options.port
    maxCount = options.maxCount
    
    if options.host == None:
        p.print_help()
    elif options.port == None:
        p.print_help
    elif options.maxCount == None:
        p.print_help()
    else:
        tcp_check(host, port, maxCount)
    
    
#TCP_ping check module
def tcp_check(host, port, maxCount):

    count = 0

    # Pass/Fail counters
    passed = 0
    failed = 0

    #Summarize Results
    def getResults():
        lRate = 0
        if failed != 0:
            lRate = failed / (count) * 100
            lRate = "%.2f" % lRate
        flt_rtd = [float(x) for x in results]
        avg_rtd = statistics.fmean(flt_rtd)
        print("\nTCP Ping Results: Connections (Total/Passed/Failed): [{:}/{:}/{:}]".format((count), passed, failed))
        print("\nLatency Metrics: \n\nMinimun: {:} ms \nAverage: {:} ms \nMaximum: {:} ms \nPacket Loss: {:}%".format(min(results), avg_rtd, max(results), str(lRate)))
       
    # Catch Ctrl-C and Exit
    def signal_handler(signal, frame):

        getResults()
        sys.exit(0)

    # Register SIGINT Handler
    signal.signal(signal.SIGINT, signal_handler)

    # Loop while less than max count or until Ctrl-C caught and creating a list with results
    results = []

    while count < maxCount:
        # Increment Counter
        count += 1

        success = False

        # New Socket
        s = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)

        # 1sec Timeout
        s.settimeout(1)

        # Start a timer
        s_start = timer()

        # Try to Connect
        try:
            s.connect((host, int(port)))
            s.shutdown(socket.SHUT_RD)
            success = True
        
        # Connection Timed Out
        except socket.timeout:
            print("Connection timed out!")
            failed += 1
        except OSError as e:
            print("OS Error:", e)
            failed += 1

        # Stop Timer
        s_stop = timer()
        s_runtime = "%.2f" % (1000 * (s_stop - s_start))
        results.append(s_runtime)

        if success:
            if port == 80:
                print("Connected to %s at Port %s (HTTP): tcp_seq=%s RTD = %s ms" % (host, port, (count-1), s_runtime))
            elif port == 443:
                print("Connected to %s at Port %s (HTTPS): tcp_seq=%s RTD = %s ms" % (host, port, (count-1), s_runtime))
            else:
                print("Connected to %s at Port %s: tcp_seq=%s RTD = %s ms" % (host, port, (count-1), s_runtime))
            passed += 1 

        # Sleep for 1sec
        if count < maxCount:
            time.sleep(1)
    
    getResults()

if __name__ == '__main__':
    # function calling
    Main()
