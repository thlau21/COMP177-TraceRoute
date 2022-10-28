from scapy.all import *
import ipaddress
import sys
from scapy.layers.inet import IP, UDP
from scapy.sendrecv import sr1
from random import randint


# random destination port for each probe
def dportRand():
    return randint(33343,33464)  

def validate_ip(ip:str):
    #try to validate ip
    try:
        valid_object = ipaddress.ip_address(ip)
        print(f"IP '{ip}' is valid!")
    except ValueError:
        print(f"IP '{ip}' is invalid!")
        sys.exit()

if __name__ == "__main__":
    destinationIP = sys.argv[1]
    validate_ip(destinationIP)
    
    maxHops = 20
    maxProbes = 1
    targetReached = False
    flag = False
    
    for TTL in range(1, maxHops+1):
        if flag is False:
            #hide verbose of scapy
            conf.verb = 0
            #create packet to send
            packetToSend = IP(ttl = TTL, dst = destinationIP)/UDP(dport = dportRand())
            #send packet
            answer = sr1(packetToSend, timeout = 1)
            
            #no reply from packet request
            if answer is None:
                print('No answer!')
                break
            #hit port unreachable
            elif (answer.type == 3):
                #target reached and TTL isn't done
                if (targetReached == True and (TTL != maxHops + 1)):
                    print(TTL, ".*")
                elif(TTL != maxHops+1):
                    print(answer.src)
                    targetReached = True
                else:
                    break
            else:
                print(TTL, ". ", answer.src)