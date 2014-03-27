#!/usr/bin/env python
#coding:utf-8

#date
start_year=input("Year Start >")
end_year=input("Year End >")
year_leap = False

def get_month_days(month,days):
    i = 0
    while (i<days):
        i+=1
        if (i<10):
             i = "0"+str(i)
        if (month<10):
            month = "0"+str(month)
        print str(start_year)+" "+str(month)+" "+str(i)
        i = int(i)
        month = int(month)

def get_year_days(year):
    month = 0
    while (month<12):
        month += 1
        if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
            days = 31
            get_month_days(month,days)
        if month==2:
            if year_leap:
                days = 29
            else:
                days = 28
            get_month_days(month,days)
        if month==4 or month==6 or month==9 or month==11:
            days = 30 
            get_month_days(month,days)

while (start_year < end_year+1):
    if start_year%400==0 or (start_year%4==0 and start_year%100!=0):
        year_leap = True
    get_year_days(start_year)
    start_year += 1
