from scapy.all import *
import ipaddress
import random
import sys
import socket
from scapy.layers.inet import IP, UDP, Ether
from scapy.sendrecv import sr, sr1, sendp, send, srp
from scapy.layers.l2 import Ether, ARP

# random destination port for each probe
def dportRand():
    return random.randint(33343,33464)  
sport = random.randint(1020, 65535)     # random high number for source port
ipInRoute = []                          # list for ip addresses found

def validate_ip(ip:str):
    #try to validate ip
    try:
        valid_object = ipaddress.ip_address(ip)
        print(f"IP '{ip}' is valid!")
    except ValueError:
        print(f"IP '{ip}' is invalid!")
        sys.exit()

# gets IP address from user   



# so I think i need to make a packet and send it
# after each time I send it, I'll record the response in the list (looking for IP addresses)
# after each time I send it, I'll increment the hops, i.e., time to live

if __name__ == "__main__":
    destinationIP = sys.argv[1]
    validate_ip(destinationIP)
    
    maxHops = 20
    maxProbes = 1
    targetReached = False
    flag = False
    
    for TTL in range(1, maxHops+1):
        if flag is False:
            conf.verb = 0
            packetToSend = IP(ttl = TTL, dst = destinationIP)/UDP(dport = dportRand())
            answer = sr1(packetToSend, timeout = 1)
            
            if answer is None:
                print('No answer!')
                break
                