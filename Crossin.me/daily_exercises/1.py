#coding:utf-8
#从1到n 取m个数 1<=m<=n
from random import randint

print "---------------------------------"

try:
    n = input("Please input number of N > ")
except NameError:
    print "Please check your input, needs number only"
    n = input("Please input number of N > ")
    
number_list = []
for i in range(1,n+1):
    number_list.append(i)
    
m = randint(1,n)
print "Get",m,"number"
get_number = []
for i in range(0,m):
    x = randint(1,n-1)
    get_number.append(number_list[x])
    
print "\nDone\n"
for i in get_number:
    print i,
    
print "\n---------------------------------"