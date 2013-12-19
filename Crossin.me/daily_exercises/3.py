#!/usr/bin/env python
#coding:utf-8
#------------------------------------------------------------------
''join([i for i in text if i.isdigit()])
#[i for i in test]这是一种生成list的方法，通过后面的if可以增加生成时的过滤条件
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
