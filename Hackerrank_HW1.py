#!/usr/bin/env python
# coding: utf-8

# # PROBLEM 1 #

# ### INTRODUCTION ###

# In[30]:


#Say “Hello, World!” with python
print("Hello, World!")


# In[31]:


#Python if-else
#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input("give me a number:").strip())

#n is odd
if n%2!=0:
    print("Weird")
#n is even
if n%2==0:  
    if (n>=2 and n<=5):
        print("Not Weird")
    
    if (n>=6 and n<=20):
        print("Weird")
        
    if n>20:
        print("Not Weird")


# In[33]:


#Arithmetic Operators

if __name__ == '__main__':
    a = int(input("write a nunber a: "))
    b = int(input("Write another number b: "))

 #(a>=1 and a<=10**10) and (b>=1 and b<=10**10): 
    print(a+b)
    print(a-b)
    print(a*b)


# In[34]:


#Python: Division
if __name__ == '__main__':
    a = int(input("Give me an integer: "))
    b = int(input("Write another integer: "))
 
#integer division
print(a//b)


# In[35]:


#float division
print(a/b)


# In[39]:


#Python: Loops
if __name__ == '__main__':
    n = int(input("give me a number: "))

 
if n>=1 and n<=20:   
    for i in range(n):
        print(i**2)
        


# In[40]:


#Print Function
if __name__ == '__main__':
    n = int(input("Write a number: "))
    
my_list=[]
for i in range(1,n+1):
    my_list.append(i)

print(*my_list,sep='')


# In[41]:


#Write a Function
def is_leap(year):
    leap = False
    
    if year%4==0:
        leap=True
        if year%100==0 and year%400!=0:
            leap=False
        else:
            leap=True  
    
    return leap

year = int(input("Write a year to find is leap year or not: "))
print(is_leap(year))


# ### Basic Data Types ###

# In[44]:


#Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input("Give number of participants n:" )) 
    #n = int(input())  
    scores = map(int, input("Give n scores for each participant:").split())
    scores = list(set(scores))
    scores.sort()
    #print(scores)
    scores.reverse()
    print("Runner up score is:", scores[1])
    #print(scores[1])

    #Find runner up score. (the one with the second best score)


# In[ ]:


#Nested List


if __name__ == '__main__':
    records=[]
    lname=[]  # list of the names 
    lscore=[]  # list of the scores 
#N=int(input())  #number of students  N<=2 and N>=5
    for _ in range(int(input("write number of students N: "))):
        name = input("Write a student name: ")
        score = float(int(input("Write studens' score: "))
        records.append([name,score])
        lname.append(name)
        lscore.append(score)
 

lscore.sort()
      
          
#print the name of student having the second lowest grade.
#first order the scores
#then print name of students    
 


# In[52]:


#Nested List

#if __name__ == '__main__':
records=[]
lname=[]  # list of the names 
lscore=[]  # list of the score
for _ in range(int(input("give number of the students n: "))):
    name = input("write a student name")
    score = float(input("write the score of the student that you wrote: "))
    #score = float(int(input("Write studens' score: "))
    records.append([name,score])
    lname.append(name)
    lscore.append(score)
 
lscore.sort()
records.sort()
print("sorted records list: ",records)      


# In[57]:


print("sorted score list is that: ", lscore)
print("max score is: ",max(lscore))


# In[3]:


#Finding the percentage

if __name__ == '__main__':
    n = int(input("number of students records: "))

    student_marks = {}  #dictionary
    for _ in range(n):
        name, *line = input("Student name and score: ").split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input("Give me a student name to calculate his avg score: ")
    
    if query_name in student_marks:
        s1=sum(student_marks[query_name]) 
        l1=len(student_marks[query_name])
        avg=s1/l1
        print(f' Average score of the student is, {avg:.2f}')


# In[28]:


#Lists
if __name__ == '__main__':
     N = int(input("please give number of the commands N: "))   #number of commands 
list2=[]

#i= #position i (index)

for i in range(N):
    comm1=input("write a command and index & number if required. ").split() 
    if comm1[0]=="insert":  #insert 3 1 (index 1, insert value 3 )
        list2.insert(int(comm1[1]),int(comm1[2]))
        print(list2)

    if comm1[0]=="print":
        print(list2)
    if comm1[0]=="remove": 
        list2.remove(int(comm1[1])) #Delete the first occurrence of integer e
        print(list2)
    if comm1[0]=="append":
        list2.append(int(comm1[1])) #append, end of the list 2
        print(list2)
    if comm1[0]=="sort":
        list2.sort()
        print(list2)
    if comm1[0]=="pop":
        list2.pop()
        print(list2)
    if comm1[0]=="reverse":    
        list2.reverse()
        print(list2)
        


# In[58]:


print(list2)


# In[3]:


#Tuples

if __name__ == '__main__':
    n = int(input("Please write the number of elements n in the tuple: "))
    integer_list = map(int, input("give elements of the tuple: ").split())
    myTuple=tuple(integer_list)
    print("Hashed of myTuple is: ",hash(myTuple))
    

#Note, Language is "pyPy3" in the Hackerrank.
#There exists an error for the Python language.


# ### STRINGS ###

# In[60]:


#String Split and Join

def split_and_join(line):
    asplit=line.split(" ")
    ajoin="-".join(asplit)
    return ajoin

if __name__ == '__main__':
    line = input("Write a sentence or something to split: ")
    result = split_and_join(line)
    print(result)


# In[62]:


#Whats your name?

def print_full_name(first, last):
    print('Hello' + ' '+ first + ' ' + last + '! You just delved into python.')
    
if __name__ == '__main__':
    first_name = input("what is your name: ")
    last_name = input("what is your surname: ")
    print_full_name(first_name, last_name)


# In[ ]:





# ### SETS ####

# In[ ]:





# ### COLLECTIONS####

# In[ ]:





# ### DATE AND TIME###

# In[ ]:





# ### EXCEPTIONS - only 1 ###

# In[ ]:





# ### BUILT - INS ###

# In[ ]:





# ### PYTHON FUNCTIONALS ###

# In[ ]:





# ### REGEX AND Pursing ###

# In[ ]:





# ### XML ###

# In[ ]:





# ### CLOSURES AND DECORATIONS ###

# In[ ]:





# ### NUMPY ###

# In[ ]:


##shape and reshape

"""
import numpy
my_array2D= numpy.array([[1, 2],[3, 4],[6,5]])
print (my_array2D.shape)     #(3, 2) -> 3 rows and 2 columns  
"""

import numpy

#1 2 3 4 5 6 7 8 9
    
inputList=list(map( int, input("Give me list of numbers").split() )) 

inputList=numpy.array(inputList)

inputList.shape=(3,3)

print(inputList)


# # PROBLEM 2 #

# In[24]:


#Birthday Cake Candles

    
 #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):

    max1=0
    count1=0
    n=int(input("give number of candles: "))
    candles=list(map(int, input("give height of candles: ").rstrip().split()))
    for el in candles:
        if el >= max1:
            max1 = el
        if el == max1:
            count1 = count1 + 1
            
    return count1
   
birthdayCakeCandles(candles)
    
##if __name__ == '__main__':


# In[22]:


# Kangoroo


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):

    stop=False
    first_multiple_input = input("give x1,v1,x2,v2 for kangoroo 1 and kangoroo 2 ").rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    #t= time 
    #x1=starting distance 1 for kangoroo 1   
    #x2: starting distance 2
    for t in range(1,10000):
        dist1=x1 +(v1*t)  #distance of kangoroo 1 
        dist2=x2 +(v2*t)  #distance of kangoroo 2
        if dist1==dist2:
            stop=True
            break
        
    if stop:
        return "YES"
    else:
        return "NO"
   

kangaroo(x1, v1, x2, v2)

    #fptr.write(result + '\n')

    #fptr.close()


# In[ ]:




