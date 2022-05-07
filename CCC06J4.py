# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 18:24:08 2021

@author: gyzou
"""

task_list = [1,2,3,4,5,6,7]
new_list = []
add_list = []
completed = "Yes"

prerequisite_list = [1,1,2,3,3]
postrequisite_list = [7,4,1,4,5]
to_be_removed = []

int1 = int(input())
int2 = int(input())

while int1 != 0 and int2 != 0:
    prerequisite_list.append(int1)
    postrequisite_list.append(int2)
    int1 = int(input())
    int2 = int(input())

while len(postrequisite_list) > 0:
    
    for k in range (len(postrequisite_list)):
        if postrequisite_list[k] in task_list:
            task_list.remove(postrequisite_list[k])
            
    if len(task_list) < 1:
        completed = "No"
        break
    else:
        new_list.append(task_list[0])
    
    for l in range (len(prerequisite_list)):
        if new_list[-1] == prerequisite_list[l]:
            to_be_removed.append(l)
    
    for m in range (len(to_be_removed)-1,-1,-1):
        prerequisite_list.pop(to_be_removed[m])
        postrequisite_list.pop(to_be_removed[m])
    
    to_be_removed = []
    task_list = []
    for n in range (1,8):
        if n in new_list:
            pass
        else:
            task_list.append(n)


if len(new_list) < 7:
    for n in range (1,8):
        if n in new_list:
            pass
        else:
            add_list.append(n)
    
    new_list.extend(add_list)


if completed == "No":
    print("Cannot complete these tasks. Going to bed.")
elif completed == "Yes":
    for i in range (0,len(new_list)):
        print(new_list[i], end = " ")
