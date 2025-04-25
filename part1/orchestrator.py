#!/usr/bin/env python
import subprocess
import os


def moveFlow(direction, curr_direction):
    if direction == curr_direction:
        return
    if direction == "n":
        os.system("sudo docker exec part1-r2-1 vtysh -c 'configure terminal' -c 'interface eth0' -c 'ip ospf cost 5' -c 'end'")
        os.system("sudo docker exec part1-r4-1 vtysh -c 'configure terminal' -c 'interface eth0' -c 'ip ospf cost 10' -c 'end'")
    
    if direction == "s":
        os.system("sudo docker exec part1-r4-1 vtysh -c 'configure terminal' -c 'interface eth0' -c 'ip ospf cost 5' -c 'end'")
        os.system("sudo docker exec part1-r2-1 vtysh -c 'configure terminal' -c 'interface eth0' -c 'ip ospf cost 10' -c 'end'")


os.system("chmod 755 dockersetup")
os.system("./dockersetup")
os.system("sudo docker compose build")
os.system("sudo docker compose up -d")
os.system("sudo docker exec part1-ha-1 route add -net 10.0.15.0/24 gw 10.0.14.10")
os.system("sudo docker exec part1-hb-1 route add -net 10.0.14.0/24 gw 10.0.15.3")
os.system("xterm &")

#tells whether traffic is on north (n) or south (s) path
curr_direction = "n"
keepGoing = True
while keepGoing:
    command = input("To change traffic flow path, type 'n' for north path and 's' for south path. Type 'exit' to stop the program.\n")
    if command == 'n' or command == 's':
        moveFlow(command, curr_direction)
        curr_direction = command
        print("current direction:", curr_direction)
    elif command == 'exit':
        keepGoing = False
    else:
        print("Unknown command")

os.system("sudo docker compose down")