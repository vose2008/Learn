#!/usr/bin/env python
#coding:utf-8

#date
year=input(">")
year_leap = False

if year%400==0 or (year%4==0 and year%100!=0):
    year_leap = True
if year_leap:
    m=0
    while (m<12):
        m+=1
        if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
            d = 0
            while (d<31):
                d+=1
                if (d<10):
                    d = "0"+str(d)
                if (m<10):
                    m = "0"+str(m)
                print str(year)+str(m)+str(d)
                d = int(d)
                m = int(m)
        if m==2:
            d = 0
            while (d<29):
                d+=1
                if (d<10):
                    d = "0"+str(d)
                if (m<10):
                    m = "0"+str(m)
                print str(year)+str(m)+str(d)
                d = int(d)
                m = int(m)
        if m==4 or m==6 or m==9 or m==11:
            d = 0
            while (d<30):
                d+=1
                if (d<10):
                    d = "0"+str(d)
                if (m<10):
                    m = "0"+str(m)
                print str(year)+str(m)+str(d)
                d = int(d)
                m = int(m)

