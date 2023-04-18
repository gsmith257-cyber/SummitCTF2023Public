from scapy.all import *
import sys

r = rdpcap(sys.argv[1])
#convert sys.argv[2] to bytes
ip = sys.argv[2]
 
a = ""
list = []
list2 = []
hexList = []
b = ""
 
for i in range(0,len(r)):
    #check if the ip is in the packet
    if ip in r[i][IP].dst: 
        b = r[i][DNSQR].qname
        #check is b is empty
        try:
            list.append((b.replace(b".",b"")))
        except:
            pass
#delete repeated elements
#join list into one string
#decode list to ascii
for i in list:
    if (i.decode('ascii')) not in list2:
        list2.append(i.decode('ascii'))

#join list2 into one string and decode from hex
print("".join(list2).encode('utf-8').decode('unicode_escape'))