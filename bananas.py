# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 16:55:27 2021

@author: gyzou
"""
def countBandS (word):
    countB = 0
    countS = 0
    for i in word:
        if i == 'B':
            countB += 1
        if i == 'S':
            countS += 1
    if countB == countS:
        return True
    else:
        return False

def find(string,char):
    placements = []
    for i in range (0,len(string)):
        if string[i] == char:
            placements.append(i)
    return placements

def remover (word,indeces):
    char_list = list(word)
    char_list.pop(indeces[1])
    char_list.pop(indeces[0])
    new_word = ""
    return(new_word.join(char_list))
            
def monkey_word(word):
    # Case 1: "A"
    if word == 'A':
        return True
    # Case 2: N's
    if word.find("N") != -1 and word.find("B") == -1 and word.find("S") == -1:
        if monkey_word(word[0:word.find("N")]) == True and monkey_word(word[word.find("N")+1:len(word)]) == True:
            return True
        else:
            return False
    # Case 3: B's and S's
    if word.find("B") != -1 and word.find("S") != -1:
        if countBandS(word) == True:
            b_positions = find(word,"B")
            s_positions = find(word,"S")
            all_positions = []
            for i in b_positions:
                for k in s_positions:
                    if i < k:
                        all_positions.append([i,k])
            smallest_difference = all_positions[0]
            all_positions.remove(all_positions[0])
            for i in range (0,len(all_positions)):
                if abs(smallest_difference[1]-smallest_difference[0]) > abs(all_positions[i][0]-all_positions[i][1]):
                    smallest_difference = all_positions[i]
                elif abs(smallest_difference[1]-smallest_difference[0]) == abs(all_positions[i][0]-all_positions[i][1]):
                    if smallest_difference[1]+smallest_difference[0] < all_positions[i][0]+all_positions[i][1]:
                       smallest_difference = all_positions[i]
            smallest_difference.sort()
            if monkey_word(word[smallest_difference[0]+1:smallest_difference[1]]) == True:
                return monkey_word(remover(word,smallest_difference))
            else:
                return False
        else:
            return False
    else:
        return False

word = input()

while word != 'X':
    if monkey_word(word) == True:
        print("YES")
    else:
        print("NO")
    word = input()

