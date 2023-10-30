#!/usr/bin/python

#import everything
from socket import *
#menus
import optparse
# import everything
from threading import *

#portscanner function
def portScan(targetHost, targetPort):
	#resolve domain name to IP address
	try:
		targetIP = gethostbyname(targetHost)
	except:
		print ('Cant Resolve Target Host %s ' %targetHost)
	try:
		targetName = gethostbyaddr(targetIP)
		print ('[+] Scan Results For: ' + targetName[0])
	except:
		print ('[+] Scan Results for: '+ targetIP) 
	setdefaulttimeout(1)
	for targetPort in targetPort:
		t = Thread(target=connectionScan, args = (targetHost,int(targetPort)))
		t.start()

#main function
def main():
	#call options for user
	parser = optparse.OptionParser('Usage of Program: ' + '-H <target host> -p <target port>')
	parser.add_option('-H', dest='targetHost', type = 'string', help= 'specify target host')
	parser.add_option('-p', dest='targetPort', type = 'string', help = 'specify target ports seperated by a comma')
	(options, args) = parser.parse_args()
	targetHost = options.targetHost
	#targetPort set to accept comma seperated input
	targetPort = str(options.targetPort).split(',')
	if (targetHost == None) | (targetPort[0] == None):
		print (parser.usage)
		exit (0)
	portScan(targetHost, targetPort)

if __name__ = '__main__' :

	main()
