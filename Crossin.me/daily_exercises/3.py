#!/usr/bin/env python
#coding:utf-8
#------------------------------------------------------------------

#------------------------------------------------------------------

text = "aAsmr3idd4bgs7Dlsf9eAF"
s = ''
for i in range(0,len(text)-1):
    try:
        int(text[i])
        s += text[i]
    except ValueError:
        pass
print s
