# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:04:43 2022

@author: gyzou
"""

def find_path (start,dest,path = []):
    path = path + [start];
    if start == dest:
        return path;
    if start not in web_graph:
        return None;
    else:
        for node in web_graph[start]:
            if node not in path:
               newpath = find_path(node,dest,path);
               if newpath: return newpath;
    return None;

def find_websites (string,start):
    char_list = [];
    new_web = "";
    current_index = 0;
    while(string[start+current_index] != '"' and string[start+current_index+1] != '>'):
        char_list.append(string[start+current_index]);
        current_index += 1;
    current_index += 2;
    return [start+current_index,new_web.join(char_list)];

web_graph = {
    };
websites = int(input());
count = 0;
website_name = True;
current_web = "";
returned_web = [];
web_list = [];
val = 0;

while (count != websites):
    line = input();
    if (website_name == True):
        web_graph[line] = [];
        current_web = line;
        website_name = False;
    if (line.find("</HTML>") != -1):
        web_graph.update({current_web: web_list});
        web_list = [];
        website_name = True;
        count += 1;
    if (line.find("<A HREF=") != -1):
        returned_web = find_websites(line,line.find("<A HREF=")+9);
        web_list.append(returned_web[1]);
        val = returned_web[0];
        returned_web = [];
        if val == len(line):
            continue;
        while (line[val:len(line)].find("<A HREF=") != -1):
            returned_web = find_websites(line,line[val:len(line)].find("<A HREF=")+9+val);
            web_list.append(returned_web[1]);
            val = returned_web[0];
            returned_web = [];
            if (line[val:len(line)].find("<A HREF=") == -1):
                break;

for i in web_graph:
    for j in range (len(web_graph.get(i))):
        print("Link from "+ i +" to " + web_graph.get(i)[j]);
        
start = "";

while (True):
    start = input();
    if (start == 'The End'):
        break;
    dest = input();
    path_exists = find_path(start,dest);
    if (path_exists == None):
        print("Can't surf from "+ start + " to " + dest + ".");
    else:
        print("Can surf from "+ start + " to " + dest + ".");
    start = "";
    dest = "";
