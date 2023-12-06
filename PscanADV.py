#!/usr/bin/python

#import everything
from socket import *
#menus
import optparse
# import everything
from threading import *

#connection scanner
def connectionScan(targetHost, targetPorts):
        try:
                sock = socket(AF_INET, SOCK_STREAM)
                sock.connect((targetHost, targetPorts))
                print('[+] {} TCP Open'.format(targetPorts))
        except:
                print('[-] {} Closed'.format(targetPorts))
        finally:
                sock.close()

#portscanner function
def portScan(targetHost, targetPorts):
	#resolve domain name to IP address
	try:
		targetIP = gethostbyname(targetHost)
	except:
		print('Cant Resolve Target Host {}'.format(targetHost))
	try:
		targetName = gethostbyaddr(targetIP)
		print('[+] Scan Results For: ' + targetName[0])
	except:
		print('[+] Scan Results for: '+ targetIP) 
		setdefaulttimeout(1)
	for targetPort in targetPorts:
		if targetPort.strip():
			t = Thread(target=connectionScan, args=(targetHost, int(targetPort)))
			t.start()

#main function
def main():
        #call options for user
        parser = optparse.OptionParser('Usage of Program: ' + '-H <target host> -p <target port>')
        parser.add_option('-H', dest='targetHost', type='string', help='specify target host')
        parser.add_option('-p', dest='targetPort', type='string', help='specify target ports separated by commas')
        (options, args) = parser.parse_args()
        targetHost = options.targetHost
        #targetPort set to accept comma-separated input
        targetPorts = str(options.targetPort).split(',')
        if (targetHost is None) or (targetPorts[0] is None):
                print(parser.usage)
                exit(0)
        portScan(targetHost, targetPorts)

if __name__ == '__main__':

        main()
