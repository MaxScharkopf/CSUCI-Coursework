"""*****************************************************************
    CS 104: Introduction to Programming
    LISTs Part2(20 points total)
    Filename: templateListsPart2_IC10_S17.py
    Date:   [YOUR DATE]
    Author: [YOUR NAME]
*****************************************************************"""

"""*****************************************************************

Write a function called "equals" that accepts 2 arguments
The two arguments will be of type list
The function should return one string, either
"Equals" or "Not Equals"

For the lists to be equal, they need to:
Have the same number of elements
Have all the elements be of the same type
Have the order fo the elements be the same

DO NOT USE "==" TO COMPARE WHOLE LISTS IN YOUR CODE, you have to rewrite this!!!
(8 points)
*****************************************************************"""
#your code goes here:


def equals(list1, list2):
    list1_Len = len(list1)  
    list2_Len = len(list2)
    
    
    if list1_Len != list2_Len:
        
        return ("Not Equals")
    
    for x in range(list1_Len):
        if list1[x] != list2[x]:       
            return ("Not Equals")
    
    
    return ("Equals")




"""*****************************************************************

Write a function called "merge" that accepts 2 arguments
The two arguments will be of type list
For simplicity sake, I'll call the two arguments 'a' and 'b'
The function will return a list
That list is the "alternating merge" of a and b

The book has a good example, but I'll add one here:
a = [1,3,5,7]
b = [2,4,6,8,9,10]
print(merge(a,b)) -> [1,2,3,4,5,6,7,8,9,10]

Make sure your function returns the "merged list"
Without returning the correct list, you will not pass the grader

(12 points)
*****************************************************************"""
#your code goes here:

def merge(list1, list2):
    list_merge = []
    
    max_len = max(len(list1), len(list2))
    
    for x in range(max_len):
        if x < len(list1):
        
            list_merge.append(list1[x])
            
        if x < len(list2):
            
            list_merge.append(list2[x])
            
            
    return list_merge

