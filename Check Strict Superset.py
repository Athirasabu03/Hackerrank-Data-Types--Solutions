#!/usr/bin/env python
# coding: utf-8

# #### Task
# You are given a set  and  other sets.
# Your job is to find whether set  is a strict superset of each of the  sets.
# 
# Print True, if  is a strict superset of each of the  sets. Otherwise, print False.
# 
# A strict superset has at least one element that does not exist in its subset.

# In[1]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(input().split())
b = True
for i in range(int(input())):
    c = set(input().split())
    if (a > c) == False:
        b = False
        break
print(b)


# In[ ]:




