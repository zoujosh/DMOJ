# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 10:09:13 2021

@author: gyzou
"""

total_lines = int(input())
friend = []
wait = []
dont_add = []
combine = []
wait_time = 1

for i in range (total_lines):
    
    command = list(input().split())
    
    if command[0] == 'R':
        for k in range (len(wait)):
            if friend[k] in dont_add:
                pass
            else:
                wait[k] += wait_time
        
        if command[1] in friend:
            dont_add.remove(command[1])
        else:
            friend.append(command[1])
            wait.append(0)       
        wait_time = 1
    
    elif command[0] == 'W':
        wait_time = int(command[1])
    
    elif command[0] == 'S':
        for k in range (len(wait)):
            if friend[k] in dont_add:
                pass
            else:
                wait[k] += wait_time
        dont_add.append(command[1])
        wait_time = 1

for i in range(len(friend)):
    if friend[i] in dont_add:
        combine.append([friend[i],wait[i]])
    else:
        combine.append([friend[i],-1])
    
combine.sort()

for i in range (len(combine)):
    print(str(combine[i][0]) + " " + str(combine[i][1]))