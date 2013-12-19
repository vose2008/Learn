#!usr/bin/env python
#coding:utf-8
#----------------------------------------------------------
sorted(set(x))
#----------------------------------------------------------

#x = raw_input('input list >')
x = '1,2,3,2,5,9,4,5,6,1,1,1'
x = x.split(',')
count = len(x) - 1
for i in range(count,0,-1):
    for j in range(0,i):
        if x[j] > x[j+1]:
            x[j],x[j+1] = x[j+1],x[j]
        if x[j] == x[j+1]:
            x.remove(x[j])
            
for i in x: 
    print i
