#!/usr/bin/env python3
"""*****************************************************************
    CS 104: Introduction to Programming
    Dictionaries(20 points total)
    Filename: template_Dictionaries_HW14.py
    Date:
    Author:

*****************************************************************"""

"""
Manage student grades. ( 20 points )
Use a dictionary to track student grades.

You are creating a grade book using a dictionary
All input will be valid, so dont worry about wrong values being passed 

Your program should manage all possible cases
for adding("A"), removing("R"), Modifying("M") a student grade, and so on.
For example:
for "A" handle a case if the student is already present, print "Student already in grades!"
for "M" handle a case if the student is not present, print "Student not found!"
for "R" handle a case when a student is not present, print "Student not found!"
Have a Quit("Q") case, that quits the loop and prints the Dictionary sorted in the format shown by the book.

You should simply print the exception cases when you run into them
Once the Quit case is met, the output format should be as follows

Student1: Grade1
Student2: Grade2

And so on
"""

#your code goes here:

gradeBook = {}   

def adding(name):            
    if name in gradeBook:
        print("Student already in grades!")       
    else:
        grade = input()
        gradeBook[name] = grade
    return

def removing(name):
    if name in gradeBook:
        del gradeBook[name]
    else:
        return print("Student not found!")
    return
       
def modifying(name):
    if name in gradeBook:
        grade = input()
        gradeBook[name] = grade        
    else:
        return print("Student not found!")
    return
    
while(True):
    

    operation = input()

    if(operation == 'A'):
        name = input() 
        adding(name)
    
    elif(operation == 'M'):
        name = input()      
        modifying(name)
        
    elif(operation == 'R'):
        name = input() 
        removing(name)
                
    elif(operation == 'Q'):
        break;

    else:
        continue
    

sorted_by_keys = dict(sorted(gradeBook.items()))

for key, value in sorted_by_keys.items():
    print(key + ": " + value)


    
    
    