![Image description](https://github.com/Despereaux222/HoneyPot-DDoS/blob/master/Infomation.png)


Project to redirect all SYN traffic from Victim to HoneyPot if Router determine that's a DDoS attack from Attacker.


TUTORIAL:
------
1. Attacker:

Download SYN_Flood_Scapy.py:

+ wget https://raw.githubusercontent.com/Despereaux222/HoneyPot-DDoS/master/SYN_Flood_Scapy.py

+ Run command: python SYN_Flood_Scapy.py (IP Victim) to DDoS Attack.

+ Example: python SYN_Flood_Scapy.py 192.168.70.102

+ Read this article to know more about this script: https://opensourceforu.com/2011/10/syn-flooding-using-scapy-and-prevention-using-iptables/

2. Router:

Download SniffnReroute.py:

+ wget https://raw.githubusercontent.com/Despereaux222/HoneyPot-DDoS/master/SYN_Flood_Scapy.py

+ Edit IP of Assets (Victim) and HoneyPot by editor (vi or vim) then run: python SniffnReroute.py and leave it.

+ Open new tab and type: sed -i 's|#net.ipv4.ip_forward=1$|net.ipv4.ip_forward=1|' /etc/sysctl.conf; sysctl -p

+ Edit destination IP in file bash by editor (vi or vim): iptables.sh then run: ./iptables.sh to set IPTables list.

3. HoneyPot:

Download Pentbox-1.8 from H4CK3RT3CH or unzip:

+ git clone https://github.com/H4CK3RT3CH/pentbox-1.8.git or unzip pentbox-1.8.zip

+ Run command: ./pentbox.rb (Choose Network Tools > HoneyPot)


VIDEO DEMO:
------
+ Port Scanning  : https://youtu.be/ysykXEn4q30
+ Detect Intruder: https://youtu.be/N3vgeJx_h5w
+ DDoS Attack    : https://youtu.be/rbulLS7ZRmI
