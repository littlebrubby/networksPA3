#!/usr/bin/env python
import subprocess
#tells whether traffic is on north (n) or south (s) path
curr_direction = "n"

def moveFlow(direction):
    if direction == curr_direction:
        return
    if direction == "n":
        subprocess.Popen("docker exec part1-r2-1 vtysh -c 'configure terminal' -c 'interface eth0' -c 'ip ospf cost 5' -c 'end'")
        subprocess.Popen("docker exec part1-r4-1 vtysh -c 'configure terminal' -c 'interface eth0' -c 'ip ospf cost 10' -c 'end'")
        curr_direction = "n"
    
    if direction == "s":
        subprocess.Popen("docker exec part1-r4-1 vtysh -c 'configure terminal' -c 'interface eth0' -c 'ip ospf cost 5' -c 'end'")
        subprocess.Popen("docker exec part1-r2-1 vtysh -c 'configure terminal' -c 'interface eth0' -c 'ip ospf cost 10' -c 'end'")
        curr_direction = "s"

#not doing these in a for loop because the networks are confusing between routers
#r1
subprocess.Popen("docker exec part1-r1-1 apt -y install curl")
subprocess.Popen("docker exec part1-r1-1 apt -y install gnupg")
subprocess.Popen("docker exec part1-r1-1 curl -s https://deb.frrouting.org/frr/keys.gpg | tee /usr/share/keyrings/frrouting.gpg > /dev/null")
subprocess.Popen("docker exec part1-r1-1 apt install lsb-release")
subprocess.Popen('docker exec part1-r1-1 FRRVER="frr-stable"')
subprocess.Popen("docker exec part1-r1-1 echo deb '[signed-by=/usr/share/keyrings/frrouting.gpg]' https://deb.frrouting.org/frr $(lsb_release -s -c) $FRRVER | tee -a /etc/apt/sources.list.d/frr.list")
subprocess.Popen("docker exec part1-r1-1 apt update && apt -y install frr frr-pythontools")
subprocess.Popen("docker cp daemons part1-r1-1/etc/frr/")
subprocess.Popen("docker exec part1-r1-1 service frr restart")
subprocess.Popen("docker exec part1-r1-1 vtysh -c 'configure terminal' -c 'router ospf' -c 'network 10.0.14.0/24 area 0.0.0.0' -c 'network 10.0.16.0/24 area 0.0.0.0' -c 'network 10.0.18.0/24 area 0.0.0.0' -c 'end'")
subprocess.Popen("docker exec part1-r1-1 vtysh -c 'configure terminal' -c 'interface eth0' -c 'ip ospf cost 5' -c 'exit' -c 'end'")
subprocess.Popen("docker exec part1-r1-1 vtysh -c 'configure terminal' -c 'interface eth1' -c 'ip ospf cost 5' -c 'exit' -c 'end'")
subprocess.Popen("docker exec part1-r1-1 vtysh -c 'configure terminal' -c 'interface eth2' -c 'ip ospf cost 5' -c 'exit' -c 'end'")

#r2
subprocess.Popen("docker exec part1-r2-1 apt -y install curl")
subprocess.Popen("docker exec part1-r2-1 apt -y install gnupg")
subprocess.Popen("docker exec part1-r2-1 curl -s https://deb.frrouting.org/frr/keys.gpg | tee /usr/share/keyrings/frrouting.gpg > /dev/null")
subprocess.Popen("docker exec part1-r2-1 apt install lsb-release")
subprocess.Popen('docker exec part1-r2-1 FRRVER="frr-stable"')
subprocess.Popen("docker exec part1-r2-1 echo deb '[signed-by=/usr/share/keyrings/frrouting.gpg]' https://deb.frrouting.org/frr $(lsb_release -s -c) $FRRVER | tee -a /etc/apt/sources.list.d/frr.list")
subprocess.Popen("docker exec part1-r2-1 apt update && apt -y install frr frr-pythontools")
subprocess.Popen("docker cp daemons part1-r2-1/etc/frr/")
subprocess.Popen("docker exec part1-r2-1 service frr restart")
subprocess.Popen("docker exec part1-r2-1 vtysh -c 'configure terminal' -c 'router ospf' -c 'network 10.0.16.0/24 area 0.0.0.0' -c 'network 10.0.17.0/24 area 0.0.0.0' -c 'end'")
subprocess.Popen("docker exec part1-r2-1 vtysh -c 'configure terminal' -c 'interface eth0' -c 'ip ospf cost 5' -c 'exit' -c 'end'")
subprocess.Popen("docker exec part1-r2-1 vtysh -c 'configure terminal' -c 'interface eth1' -c 'ip ospf cost 5' -c 'exit' -c 'end'")

#r3
subprocess.Popen("docker exec part1-r3-1 apt -y install curl")
subprocess.Popen("docker exec part1-r3-1 apt -y install gnupg")
subprocess.Popen("docker exec part1-r3-1 curl -s https://deb.frrouting.org/frr/keys.gpg | tee /usr/share/keyrings/frrouting.gpg > /dev/null")
subprocess.Popen("docker exec part1-r3-1 apt install lsb-release")
subprocess.Popen('docker exec part1-r3-1 FRRVER="frr-stable"')
subprocess.Popen("docker exec part1-r3-1 echo deb '[signed-by=/usr/share/keyrings/frrouting.gpg]' https://deb.frrouting.org/frr $(lsb_release -s -c) $FRRVER | tee -a /etc/apt/sources.list.d/frr.list")
subprocess.Popen("docker exec part1-r3-1 apt update && apt -y install frr frr-pythontools")
subprocess.Popen("docker cp daemons part1-r3-1/etc/frr/")
subprocess.Popen("docker exec part1-r3-1 service frr restart")
subprocess.Popen("docker exec part1-r3-1 vtysh -c 'configure terminal' -c 'router ospf' -c 'network 10.0.15.0/24 area 0.0.0.0' -c 'network 10.0.18.0/24 area 0.0.0.0' -c 'network 10.0.19.0/24 area 0.0.0.0' -c 'end'")
subprocess.Popen("docker exec part1-r3-1 vtysh -c 'configure terminal' -c 'interface eth0' -c 'ip ospf cost 5' -c 'exit' -c 'end'")
subprocess.Popen("docker exec part1-r3-1 vtysh -c 'configure terminal' -c 'interface eth1' -c 'ip ospf cost 5' -c 'exit' -c 'end'")
subprocess.Popen("docker exec part1-r3-1 vtysh -c 'configure terminal' -c 'interface eth2' -c 'ip ospf cost 5' -c 'exit' -c 'end'")

#r4
subprocess.Popen("docker exec part1-r4-1 apt -y install curl")
subprocess.Popen("docker exec part1-r4-1 apt -y install gnupg")
subprocess.Popen("docker exec part1-r4-1 curl -s https://deb.frrouting.org/frr/keys.gpg | tee /usr/share/keyrings/frrouting.gpg > /dev/null")
subprocess.Popen("docker exec part1-r4-1 apt install lsb-release")
subprocess.Popen('docker exec part1-r4-1 FRRVER="frr-stable"')
subprocess.Popen("docker exec part1-r4-1 echo deb '[signed-by=/usr/share/keyrings/frrouting.gpg]' https://deb.frrouting.org/frr $(lsb_release -s -c) $FRRVER | tee -a /etc/apt/sources.list.d/frr.list")
subprocess.Popen("docker exec part1-r4-1 apt update && apt -y install frr frr-pythontools")
subprocess.Popen("docker cp daemons part1-r4-1/etc/frr/")
subprocess.Popen("docker exec part1-r4-1 service frr restart")
subprocess.Popen("docker exec part1-r4-1 vtysh -c 'configure terminal' -c 'router ospf' -c 'network 10.0.16.0/24 area 0.0.0.0' -c 'network 10.0.17.0/24 area 0.0.0.0' -c 'end'")
subprocess.Popen("docker exec part1-r4-1 vtysh -c 'configure terminal' -c 'interface eth0' -c 'ip ospf cost 10' -c 'exit' -c 'end'")
subprocess.Popen("docker exec part1-r4-1 vtysh -c 'configure terminal' -c 'interface eth1' -c 'ip ospf cost 5' -c 'exit' -c 'end'")

#connect endpoints
subprocess.Popen("docker exec part1-ha-1 route add -net 10.0.15.0/24 gw 10.0.14.10")
subprocess.Popen("docker exec part1-hb-1 route add -net 10.0.14.0/24 gw 10.0.15.3")

keepGoing = True
while keepGoing:
    command = input("To change traffic flow path, type 'n' for north path and 's' for south path. Type 'exit' to stop the program.")
    if command == 'n' or command == 's':
        moveFlow(command)
        print("current direction:", curr_direction)
    elif command == 'exit':
        keepGoing = False
    else:
        print("Unknown command")