#!/usr/bin/python

import socket

def retBanner(ip, port):
    try:
        timeout = 2  # Set the timeout to 2 seconds
        socket.setdefaulttimeout(timeout)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except ConnectionRefusedError:
        return None  # Ignore "Connection refused" errors
    except Exception as e:
        print("Error: " + str(e))
        return None

def main():
    ip = input('[*] Enter target IP: ')
    print(f"Scanning {ip}...")
    for port in range(1, 1001):  # Scan ports from 1 to 1000
        banner = retBanner(ip, port)
        if banner:
            try:
                decoded_banner = banner.decode('utf-8')
                decoded_banner = decoded_banner.strip()  # Strip newline characters
            except UnicodeDecodeError:
                decoded_banner = banner.decode('latin-1')  # Try using latin-1 encoding if utf-8 fails
                decoded_banner = decoded_banner.strip()  # Strip newline characters
            print(f"[+]{ip}:{port}: {decoded_banner}")

main()
