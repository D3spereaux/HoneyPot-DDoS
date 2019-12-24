iptables --table nat --flush; iptables -t nat -A PREROUTING -p all -s gateway -d gateway -j ACCEPT -m limit --limit 25/m --limit-burst 100; iptables -t nat -A PREROUTING -p all -s gateway -d gateway -j DNAT --to-destination 192.168.90.102; iptables -t nat -L



iptables -t nat -A PREROUTING -p all -d 192.168.70.102 -j ACCEPT -m limit --limit 25/m --limit-burst 100; iptables -t nat -A PREROUTING -p all -d 192.168.70.102 -j DNAT --to-destination 192.168.70.200