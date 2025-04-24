#!/usr/bin/env python
import subprocess
import os


def moveFlow(direction, curr_direction):
    if direction == curr_direction:
        return
    if direction == "n":
        os.system("docker exec part1-r2-1 vtysh -c 'configure terminal' -c 'interface eth0' -c 'ip ospf cost 5' -c 'end'")
        os.system("docker exec part1-r4-1 vtysh -c 'configure terminal' -c 'interface eth0' -c 'ip ospf cost 10' -c 'end'")
    
    if direction == "s":
        os.system("docker exec part1-r4-1 vtysh -c 'configure terminal' -c 'interface eth0' -c 'ip ospf cost 5' -c 'end'")
        os.system("docker exec part1-r2-1 vtysh -c 'configure terminal' -c 'interface eth0' -c 'ip ospf cost 10' -c 'end'")

#tells whether traffic is on north (n) or south (s) path
curr_direction = "n"
keepGoing = True
while keepGoing:
    command = input("To change traffic flow path, type 'n' for north path and 's' for south path. Type 'exit' to stop the program.")
    if command == 'n' or command == 's':
        moveFlow(command, curr_direction)
        curr_direction = command
        print("current direction:", curr_direction)
    elif command == 'exit':
        keepGoing = False
    else:
        print("Unknown command")