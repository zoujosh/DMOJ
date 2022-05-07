# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 22:07:19 2021

@author: gyzou
"""
def knighthop(x3,y3,steps):
    if x3 >= 1 and x3 <= 8 and y3 >= 1 and y3 <= 8 and steps < board[x3][y3]:
      board[x3][y3] = steps
      knighthop(x3+2,y3+1,steps+1)
      knighthop(x3+2,y3-1,steps+1)
      knighthop(x3-2,y3+1,steps+1)
      knighthop(x3-2,y3-1,steps+1)
      knighthop(x3+1,y3+2,steps+1)
      knighthop(x3-1,y3+2,steps+1)
      knighthop(x3+1,y3-2,steps+1)
      knighthop(x3-1,y3-2,steps+1)
      
x1,y1 = input().split() 
x2,y2 = input().split() 

x1,x2,y1,y2 = int(x1),int(x2),int(y1),int(y2)

board = []

for i in range(9):
  board.append([100,100,100,100,100,100,100,100,100])

knighthop(x1,y1,0)

print(board[x2][y2])
        
        
    
