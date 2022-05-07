# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 11:38:05 2022

@author: gyzou
"""

equivalent_num = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000}

prev_num = 2000;
a_num = input();
a_list = list(a_num);
b_list = [];
op_list = [];
count = 0;

for i in range (int(len(a_list)/2)):
    #print(a_list[i*2+1]);
    b_list.append(a_list[i*2+1]);

for i in range (1,len(b_list)):
    if (equivalent_num.get(b_list[i]) > equivalent_num.get(b_list[i-1])):
        op_list.append('-');
    else:
        op_list.append('+');
op_list.append('+');
        
for i in range (int(len(a_list)/2)):
    if (op_list[i] == '+'):
        count += int(a_list[i*2])*equivalent_num.get(a_list[i*2+1]);
    else:
        count -= int(a_list[i*2])*equivalent_num.get(a_list[i*2+1]);

print(count);
