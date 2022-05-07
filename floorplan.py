# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 16:19:07 2022

@author: gyzou
"""

def in_room(x,y):
    if (floor_plan[x][y] == '.' and checked[x][y] == False):
        checked[x][y] = True;
        return True;
    else:
        return False;

def find_area(x,y):
    room_tiles = [];
    area = 1;       
    if (y < columns - 1 and in_room(x,y+1)):    
        room_tiles.append([x,y+1]);
        area += 1;
    if (y > 0 and in_room(x,y-1)):
        room_tiles.append([x,y-1]);
        area += 1;
    if (x < rows - 1 and in_room(x+1,y)):
        room_tiles.append([x+1,y]);
        area += 1;
    if (x > 0 and in_room(x-1,y)):
        room_tiles.append([x-1,y]);
        area += 1;
       
    while (len(room_tiles) > 0):
        tile = room_tiles.pop(0);
        if (tile[1] < columns-1 and in_room(tile[0],tile[1]+1)):
                room_tiles.append([tile[0],tile[1]+1]);
                area += 1;
        if (tile[1] > 0 and in_room(tile[0],tile[1]-1)):
                room_tiles.append([tile[0],tile[1]-1]);
                area += 1;
        if (tile[0] < rows-1 and in_room(tile[0]+1,tile[1])):
                room_tiles.append([tile[0]+1,tile[1]]);
                area += 1;
        if (tile[0] > 0 and in_room(tile[0]-1,tile[1])):
                room_tiles.append([tile[0]-1,tile[1]]);
                area += 1;
                
    return area;

flooring = int(input());
rows = int(input());
columns = int(input());
count = 0;
checked = [];
checked_row = [];
floor_plan = [];
room_area = [];

for i in range(rows):
  checked_row = [];
  floor_plan.append(input());
  for i in range(columns):
    checked_row.append(False);
  checked.append(checked_row);

for i in range (rows):
    for j in range (columns):
        if (checked[i][j] == False and floor_plan[i][j] == '.'):
            checked[i][j] = True;
            room_area.append(find_area(i,j));

room_area.sort();

for i in range (len(room_area)-1,-1,-1):
    if (room_area[i] <= flooring):
        count += 1;
        flooring -= room_area[i];
    else:
        break;

if (count == 1):
    print("1 room, "+str(flooring)+" square metre(s) left over");
else:
    print(str(count) + " rooms, "+str(flooring)+" square metre(s) left over");