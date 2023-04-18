import base64
import random
#import pcapwriter
from scapy.all import *
#import IP/UDP/DNS

#Generate random text for the flag

flag_text = "The flag you have been waiting for is ... Pausing for dramatic effect ... : SummitCTF{Sus_D0ma1n_n4mes}"
#Encode the flag text in base64

encoded_flag = base64.b64encode(flag_text.encode())
#Split the encoded flag into 12 character chunks

flag_chunks = [encoded_flag[i:i+12] for i in range(0, len(encoded_flag), 12)]
#Create a new PCAP file using scapy

pcap_file = PcapWriter("EscapingTheMatrix.pcap", append=True, sync=True)

#create C2 domain name from rand
domain = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(12))

#Create a new DNS packet for each chunk of the flag
#open the pcap file
pcap = "EscapingTheMatrix.pcap"

for chunk in flag_chunks:
    #write the packet to the pcap file
    packet = IP(dst="32.31.30.29")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname=chunk.decode() + "." + domain + ".summit"))
    wrpcap(pcap, packet, append=True)
    #write random packets to the pcap file
    randInt = random.randint(1, 100)
    #create random IP addresses
    randIP = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    #create random domain name
    domainName = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(12))
    for i in range(randInt):
        randSubdomian = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(12))
        packet2 = IP(dst=randIP)/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname=randSubdomian + "." + domainName + ".summit"))
        wrpcap(pcap, packet2, append=True)