#!/usr/bin/python

#import everything
from socket import *
#menus
import optparse
# import everything
from threading import *

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
	#portScan(targetHost, targetPort)


main()
