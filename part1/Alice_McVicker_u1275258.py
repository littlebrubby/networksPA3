#!/usr/bin/env python
import sys
import os

if len(sys.argv) > 1:
    if sys.argv[1] == "-h":
        print("only use one argument at a time, or none")
        print()
        print("-h       help menu options")
        print("-build   construct network topology only")
        print("-ospf    construct topology and configure")
        print("-route   above and add routes to hosts")
        print("-run     above and allow orchestration")
        print("no args  same as -run")
        sys.exit()
    elif sys.argv[1] == "-build":
        os.system("chmod 755 dockersetup")
        os.system("./dockersetup")
        os.system("cd build-only && sudo docker compose build && sudo docker compose up -d")
        sys.exit()
    elif sys.argv[1] == "-ospf":
        os.system("chmod 755 dockersetup")
        os.system("./dockersetup")
        os.system("sudo docker compose build")
        os.system("sudo docker compose up -d")
        sys.exit()
    elif sys.argv[1] == "-route":
        os.system("chmod 755 dockersetup")
        os.system("./dockersetup")
        os.system("sudo docker compose build")
        os.system("sudo docker compose up -d")
        os.system("sudo docker exec part1-ha-1 route add -net 10.0.15.0/24 gw 10.0.14.10")
        os.system("sudo docker exec part1-hb-1 route add -net 10.0.14.0/24 gw 10.0.15.3")
        sys.exit()
    elif sys.argv[1] == "-run":
        pass
    else:
        print("Unknown command.")
        sys.exit()


def moveFlow(direction, curr_direction):
    if direction == curr_direction:
        return
    if direction == "n":
        os.system("sudo docker exec part1-r2-1 vtysh -c 'configure terminal' -c 'interface eth0' -c 'ip ospf cost 5' -c 'end'")
        os.system("sudo docker exec part1-r2-1 vtysh -c 'configure terminal' -c 'interface eth1' -c 'ip ospf cost 5' -c 'end'")
        os.system("sudo docker exec part1-r4-1 vtysh -c 'configure terminal' -c 'interface eth0' -c 'ip ospf cost 10' -c 'end'")
        os.system("sudo docker exec part1-r4-1 vtysh -c 'configure terminal' -c 'interface eth1' -c 'ip ospf cost 10' -c 'end'")
    
    if direction == "s":
        os.system("sudo docker exec part1-r4-1 vtysh -c 'configure terminal' -c 'interface eth0' -c 'ip ospf cost 5' -c 'end'")
        os.system("sudo docker exec part1-r4-1 vtysh -c 'configure terminal' -c 'interface eth1' -c 'ip ospf cost 5' -c 'end'")
        os.system("sudo docker exec part1-r2-1 vtysh -c 'configure terminal' -c 'interface eth0' -c 'ip ospf cost 10' -c 'end'")
        os.system("sudo docker exec part1-r2-1 vtysh -c 'configure terminal' -c 'interface eth1' -c 'ip ospf cost 10' -c 'end'")


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