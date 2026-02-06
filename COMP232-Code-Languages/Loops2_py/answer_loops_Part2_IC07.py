"""
*************************************************************
    CS 104: Introduction to Programming
    Loops Part2(23 points total)
    Filename: loops_Part2_Template_IC07.py
    Date:   [YOUR DATE]
    Author: [YOUR NAME]
    (20 points)
**************************************************************"""

"""*****************************************************************
P4.3 page 230, Write a program that reads a line of input and prints(10 points)

Notes:

1. Promt the user just ONCE!
2. Make sure your print the output in one line.
3. You have to output your answer on a new line every time.
For example:
a
b
c
d
e

4. for problem "c" and "d": vowels = "aeiouAEIOU"
**************************************************************"""


vowels = "aeiouAEIOU"
string = input()
copy = ""
"""a. Uppercase Letters in String (2 points)"""
 ##your code goes here:

for char in string:
    if char.isupper():
        print(char, end ="")        

print("")                  

"""b. Every second letter of the string. (2 points)"""
  ##your code goes here:
for i in range(len(string)):
    if i%2 == 1:
        print(string[i], end ="")

print("")


"""c. The string with all vowels replaced by an underscore. (2 points)"""
  ##your code goes here:
for char in string:
    if char in vowels:
        copy += "_"
    else:
        copy += char
            
print(copy)



"""d. The number of digits in the string. (2 points)"""
  ##your code goes here:
count = 0
for char in string:
    if char.isdigit():
        count += 1
print(count)


"""e. The poisition of all vowels in the string. 
Print the positions separated by a space. Example: 1 5 10 35 """
##your code goes here:
count = 0
for char in string:
    if char in vowels:
        print(count, end=" ")      
    count += 1






print("-" * 30)
"""*****************************************************************
P4.6 page 230, Minimum Value (4 points)
IMPORTANT: Make the loop break when a "q" is entered.
*****************************************************************"""
 ## your code goes here:
count = 0
stack = []
while (True):
    noqplease = input()
    for char in noqplease:
        if char == 'q':
            break
    else:
        stack.append(noqplease) 
        continue
    break 
print(stack.pop())
    
print("-" * 30)
"""*****************************************************************
(6 points) Write a Python program to construct the following pattern, using a nested loop number. 
Expected Output: 
1
22
333
4444
55555
666666
7777777
88888888
999999999

**************************************************************"""

 ## your code goes here:
count = 0
for i in range(1, 10):  
    for j in range(i):
        print(i, end="") 
    print("")