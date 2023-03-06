#!/usr/bin/env python
# coding: utf-8

# #### TASK
# You are given a set  and  number of other sets. These  number of sets have to perform some specific mutation operations on set .
# 
# Your task is to execute those operations and print the sum of elements from set .
# 
# #### Input Format
# 
# The first line contains the number of elements in set .
# The second line contains the space separated list of elements in set .
# The third line contains integer , the number of other sets.
# The next  lines are divided into  parts containing two lines each.
# The first line of each part contains the space separated entries of the operation name and the length of the other set.
# The second line of each part contains space separated list of elements in the other set.
# 
# #### Output Format
# 
# Output the sum of elements in set A .

# In[2]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
m = input()
a = set(int(x) for x in input().split(' '))

n = int(input())
for m in range(n):
    op, m = input().split(' ')
    b = set(int(x) for x in input().split(' '))
    if op == "update":
        a |= b
    elif op == "intersection_update":
        a &= b
    elif op == "difference_update":
        a -= b
    elif op == "symmetric_difference_update":
        a ^= b

print(sum(a))
             


# In[ ]:




