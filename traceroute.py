#from scapy.all import *
#import netifaces
import ipaddress
import random

# random destination port for each probe
def dportRand():
    return random.randint(3343,33464)  
sport = random.randint(1020, 65535)     # random high number for source port
ipInRoute = []                          # list for ip addresses found

# gets IP address from user   
# checks that destIP is a valid IP address
ipaddress.ip_address(input("Enter destination IP address: "))

# so I think i need to make a packet and send it
# after each time I send it, I'll record the response in the list (looking for IP addresses)
# after each time I send it, I'll increment the hops, i.e., time to live

hops = 0
while hops < 20:


    ipInRoute.append(hops)
>>>>>>> 782a2c53d206ce2e0511f6ff4acb43e9d6dc430e
    hops += 1