#!/usr/bin/python

import socket
import os
import sys

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print ("[-] File Does Not Exist")
            exit(0)
        if not os.access(filename, os.R_OK):
            print("Access Denied")
            exit(0) 
    else:
        print ('[-] Usage: ' +str(sys.argv[0]+ "<vuln filename"))
        exit (0)

    portlist = list(range(1, 1001))  # Creates a list of numbers from 1 to 1000
    for x in range(1,255):
        ip = '192.168.1' + str(x)
        for port in portlist:
            banner = retBanner(ip,port)
            if banner:
                print ('[+]' + ip + "/" + str(port) + " : " + banner)
                checkVulns(banner, filename)
    