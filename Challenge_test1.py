# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 10:58:12 2019

@author: Ta Tri Nghia
"""

input_string = input("enter input:")

output_bracket = str()

temp_close_bracket = []
temp_open_bracket = []

count_close_bracket = 0
count_open_bracket = 0

balance = 0
check = True
#last_close_position = []
last_open_position = []

result = "Y"


for i in input_string:
    if (i =="{") or (i == "}") or (i =="[") or (i == "]") or (i == "(") or (i == ")"):
        output_bracket = output_bracket + i

for i in range(0, len(output_bracket)):
    if (output_bracket[i] == "{") or (output_bracket[i] == "[") or (output_bracket[i] == "("):
        balance += 1

for i in range(0, len(output_bracket)):
    
    if (output_bracket[0] == "}") or (output_bracket[0] == "]") or (output_bracket[0] == ")"):
        check = False
        balance = 0
        break
    
    if (output_bracket[i] == "}") or (output_bracket[i] == "]") or (output_bracket[i] == ")"):
        temp_close_bracket.append(output_bracket[i])
        count_close_bracket += 1
       # last_close_position = i       
                  
        for j in range(i, 0, -1):
            if (output_bracket[j-1] == "{") or (output_bracket[j-1] == "[") or (output_bracket[j-1] == "("):
                if (j-1) not in last_open_position:
                    last_open_position.append(j-1)
                    temp_open_bracket.append(output_bracket[j-1])
                    count_open_bracket += 1
                    break


if (check == False) or (balance != count_close_bracket):         
    result = "N"

elif count_open_bracket != count_close_bracket:
    result = "N"

else:
    for i in range(0,count_open_bracket):
        if temp_open_bracket[i] == "(" and temp_close_bracket[i] == ")":
            pass
        elif temp_open_bracket[i] == "[" and temp_close_bracket[i] == "]":
            pass
        elif temp_open_bracket[i] == "{" and temp_close_bracket[i] == "}":
            pass
        else:
            result = "N"
            break
       
print(result + " " + output_bracket)