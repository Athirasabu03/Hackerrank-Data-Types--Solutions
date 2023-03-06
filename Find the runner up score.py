#!/usr/bin/env python
# coding: utf-8

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    b = []
    for i in arr:
        b.append(i)
    m = max(b)
    c = []
    while m in b:    
        b.remove(m)
    print(max(b))

