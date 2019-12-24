#!/usr/bin/env python

import sys
from scapy.all import *

flop = "false"
flopCount = 0
assets = "192.168.70.102"
honeypot = "192.168.70.200"

def pkt_summary(pkt):
	global flop
	global flopCount
	global honeypot
	global assets
	if IP in pkt:
		if pkt[IP].dst == assets:
			flop = "false"
			print pkt[IP].src + " to Victim"
		if pkt[IP].dst == honeypot and flop == "false":
			flop = "true"
			flopCount = flopCount + 1
			print pkt[IP].src + " to HoneyPot"
			print flopCount
			if flopCount == 10:
				print "REROUTE ALL ATTACKS TO HONEYPOT"
				os.system("iptables -t nat -D PREROUTING 1")
				sys.exit()
sniff(prn=pkt_summary)
