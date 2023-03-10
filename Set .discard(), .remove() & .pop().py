#!/usr/bin/env python
# coding: utf-8

# #### Task
# You have a non-empty set , and you have to execute  commands given in  lines.
# 
# The commands will be pop, remove and discard.
# 
# #### Input Format
# 
# The first line contains integer , the number of elements in the set .
# The second line contains  space separated elements of set . All of the elements are non-negative integers, less than or equal to 9.
# The third line contains integer , the number of commands.
# The next  lines contains either pop, remove and/or discard commands followed by their associated value.
# 
# 
# 
# 
# 
# #### Output Format
# 
# Print the sum of the elements of set  on a single line.

# In[1]:


n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    a = input().split()
    if a[0] == 'pop':
        s.pop()
    elif a == 'remove':
        s.remove(int(a[1]))
    else:
        s.discard(int(a[1]))
print(sum(s))


# In[ ]:




