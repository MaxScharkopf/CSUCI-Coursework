#!/usr/bin/python3

"""
*****************************************************************
CS 104: Introduction to Programming
Decisions Part 1(20 points total) +5 EC
Filename: decisions_Template_Part1_HW_S17_I.py
Date: [YOUR DATE]
Author: [YOUR NAME]
*****************************************************************

Letter Grade to Number (8 points)
Given a single letter grade, calculate its equivalent Grade Point Value
A -> 4.0
B -> 3.0
C -> 2.0
D -> 1.0
F -> 0.0

if the grade letter has a plus or minus symbol ("+,-") after it most but
not all of the Grade Point Values will be adjusted
by 0.3
Edge cases to consider:
    A+ -> 4.0
    F+ -> 0.0
    F- -> 0.0
"""
#your code goes here
grade = input()

if(grade[0] == 'A'):
    if(grade[1] == None):
      print("4.0")  
    elif (grade[1] == '-'):
      print("3.7")
    else:
      print("4.0")
      
elif(grade[0] == 'B'):
    if(grade[1] == None):
      print("3.0")   
    elif(grade[1] == '+'):
      print("3.3")
    else:
      print("2.7")        
      
elif(grade[0] == 'C'):
    if(grade[1] == None):
      print("2.0")   
    elif(grade[1] == '+'):
      print("2.3")
    else:
      print("1.7")        
          
elif(grade[0] == 'D'):
    if(grade[1] == None):
      print("1.0")   
    elif(grade[1] == '+'):
      print("1.3")
    else:
      print("0.7")        
        
else:
      print("0.0")        
   
      
# End of Problem 1
print("-"*30)


"""
##Sort Three Strings Lexicographically (12 points)
Given 3 Strings, (input is separated by newlines) sort the Strings in
Lexicographically (also called Alphabetical) order.
Output is expected to be all on one line delimited by a single space.
 
A hint: have three variables: first, second and third as containers.
Then order the strings using "ifs" statements, so that first comes before
second, which comes before
third.

Extra credit (5 points) - solve this problem in 3 lines and 3 comparisons.
Do not use the list class.
"""
#your code goes here
first = input()
second = input()
third = input()

if(first < second < third):
    print(first +" "+ second +" "+third)
elif(first < third < second):
    print(first +" "+ third +" "+ second)   
elif(second < third < first):
    print(second +" "+ third +" "+ first)   
elif(second < first < third):
    print(second +" "+ first +" "+ third)  
elif(third < second < first):
    print(third +" "+ second +" "+ first)   
else:
    print(third +" "+ first +" "+ second)   


#End of Problem 2



