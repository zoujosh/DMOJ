# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 10:32:54 2021

@author: gyzou
"""

crossed_blocks =[[0,[-1,-3]],[[0,3],-3],[3,[-3,-5]],[[3,5],-5],[5,[-3,-5]],[[5,7],-3],[7,[-3,-7]],[[-1,7],-7],[-1,[-5,-7]]]
movement_list = []
current_position = [-1,-5]
crossed = []
count_to_stop = 0
no_danger = True

def inrange (integer,my_list):
    my_list.sort()
    if integer >= my_list[0] and integer <= my_list[1]:
        return True
    else:
        return False

def intersected (first_list):
    # Example: [-3,-5]
    for i in range (len(crossed_blocks)):
        # if there is an element in crossed_blocks with first element is an int, equals 3 and -5 is in between the list of numbers in the second list
        if type(crossed_blocks[i][0]) == int and first_list[0] == crossed_blocks[i][0] and inrange(first_list[1],crossed_blocks[i][1]) == True:
            return True
        # if thre is an element in crossed_blocks with second element is an int, equals -5 and 3 is in between the list of numbers in the first list
        if type(crossed_blocks[i][1]) == int and first_list[1] == crossed_blocks[i][1] and inrange(first_list[0],crossed_blocks[i][0]) == True:
            return True
    
    return False
            
command = list(input().split())

while command[0] != 'q' and count_to_stop < 1:
    command[1] = int(command[1])
    # l 2
    if command[0] == 'l' and no_danger == True:
        # [[-1,-3],-5]
        crossed = [[current_position[0],current_position[0]-command[1]],current_position[1]]
        # -3 to -2
        for i in range (crossed[0][1],crossed[0][0]):
            if intersected([i,current_position[1]]) == True:
                no_danger = False
        
        crossed_blocks.append(crossed)
        crossed = []
        if no_danger == False:
            movement_list.append([current_position[0]-command[1],current_position[1],"DANGER"])
            count_to_stop += 1
        else:
            movement_list.append([current_position[0]-command[1],current_position[1],"safe"])
        
        current_position = [current_position[0]-command[1],current_position[1]]
    
    if command[0] == 'r' and no_danger == True:
        # r 2: [[-1,1],-5]
        crossed = [[current_position[0],current_position[0]+command[1]],current_position[1]]
        # 0 to 1
        for i in range (crossed[0][0] + 1,crossed[0][1] + 1):
            if intersected([i,current_position[1]]) == True:
                no_danger = False
        
        crossed_blocks.append(crossed)
        crossed = []
        if no_danger == False:
            movement_list.append([current_position[0]+command[1],current_position[1],"DANGER"])
            count_to_stop += 1
        else:
            movement_list.append([current_position[0]+command[1],current_position[1],"safe"])
        
        current_position = [current_position[0]+command[1],current_position[1]]
    
    if command[0] == 'u' and no_danger == True:
        # u 2: [-1,[-5,-3]]
        crossed = [current_position[0],[current_position[1],current_position[1]+command[1]]]
        # -4 to -3
        for i in range (crossed[1][0]+1,crossed[1][1] + 1):
            if intersected([current_position[0],i]) == True:
                no_danger = False
        
        crossed_blocks.append(crossed)
        crossed = []
        if no_danger == False:
            movement_list.append([current_position[0],current_position[1]+command[1],"DANGER"])
            count_to_stop += 1
        else:
            movement_list.append([current_position[0],current_position[1]+command[1],"safe"])
        
        current_position = [current_position[0],current_position[1]+command[1]]

    if command[0] == 'd' and no_danger == True:
        # d 2: [-1,[-5,-7]]
        crossed = [current_position[0],[current_position[1],current_position[1]-command[1]]]
        # -7 to -6
        for i in range (crossed[1][1],crossed[1][0]):
            if intersected([current_position[0],i]) == True:
                no_danger = False
        
        crossed_blocks.append(crossed)
        crossed = []
        if no_danger == False:
            movement_list.append([current_position[0],current_position[1]-command[1],"DANGER"])
            count_to_stop += 1
        else:
            movement_list.append([current_position[0],current_position[1]-command[1],"safe"])
        
        current_position = [current_position[0],current_position[1]-command[1]]
    
    command = list(input().split())

for i in range (len(movement_list)):
    print(str(movement_list[i][0]) + " " + str(movement_list[i][1]) + " " + movement_list[i][2])  