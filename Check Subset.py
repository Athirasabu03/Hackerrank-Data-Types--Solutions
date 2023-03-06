#!/usr/bin/env python
# coding: utf-8

# #### Task
# You are given two sets,  and .
# Your job is to find whether set  is a subset of set .
# 
# If set  is subset of set , print True.
# If set  is not a subset of set , print False.

# In[1]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    a = int(input())
    m = set(input().split()) 
    b = int(input())
    n = set(input().split())
    print(m.issubset(n))


# In[ ]:




