#!/usr/bin/python

import socket

def retBanner(ip, port):
    try:
        timeout = 5  # Set the timeout to 5 seconds
        socket.setdefaulttimeout(timeout)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except Exception as e:
        print("Error: " + str(e))
        return

def main():
    port = 22
    ip = "192.168.1.108"
    timeout = 5  # Set the timeout to 5 seconds
    print(f"Scanning {ip}:{port} with a timeout of {timeout} seconds...")
    for remaining in range(timeout, 0, -1):
        print(f"Timeout in {remaining} seconds...", end='\r')
        banner = retBanner(ip, port)
        if banner:
            print(f"[+]{ip}:{port}: {banner.decode('utf-8')}")
            break
    else:
        print("Timeout reached. No response.")

main()
