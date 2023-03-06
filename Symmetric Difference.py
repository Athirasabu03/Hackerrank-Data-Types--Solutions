#!/usr/bin/env python
# coding: utf-8

# #### Task
# Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.
# 
# #### Input Format
# 
# The first line of input contains an integer, .
# The second line contains  space-separated integers.
# The third line contains an integer, .
# The fourth line contains  space-separated integers.
# 
# #### Output Format
# 
# Output the symmetric difference integers in ascending order, one per line

# In[1]:


# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
N_list = map(int, input().split(' '))
M = int(input())
M_list = map(int, input().split(' '))

N_set = set(N_list)
M_set = set(M_list)

tmp_set1 = N_set.difference(M_set)
tmp_set2 = M_set.difference(N_set)
result = tmp_set1.union(tmp_set2)
result = sorted(result)

for el in result:
    print(el)
                   


# In[ ]:




