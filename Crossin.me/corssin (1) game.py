#coding:utf-8
import random 
name = raw_input("Please enter player name:")
#Read scores file
socres = file('e:/scores.txt')
socre = socres.readlines()
socres.close()
#split name times and right_times
player = {} 
for i in socre:
    b=i.split()
    player[b[0]]=b[1:]
# get.()
get = player.get(name)
if player.get(name)==None:
    get = [0,0,0]
    print 'Player creat ....'
else:
    print 'Player load .....'
    print name+str(get)
#Game
times =0
answer_times =0
right_times =0
go_on = True
while go_on:
    answer = random.randint(1,5)
    times += 1
    right = True
    print "Game Start! "
    while right:
        a = int(raw_input(">"))
        if a > answer:
            print "It's too big"
            answer_times += 1
        elif a < answer:
            print "It's too less"
            answer_times += 1
        elif a == answer:
            print "Bingo!"
            answer_times += 1
            right_times += 1
            right = False
    print 'Go On Game? 1 or 0'
    b = int(raw_input(">"))
    if b == 1:
        right = True
        times += 1
    elif b == 0:
        go_on = False
    else:
        go_on = False
#Rank
right_times_0 = get[2]
if right_times_0 > right_times:
    print "New Rank %s"%name
    socres = file('e:/scores.txt','w')
    player[name] = [str(times), str(answer_times), str(right_times)]
    result=''
    for i in player:
        line = i + " "+' '.join(player[i])+"\n"
        result += line
    socres.write(result)
else:
    pass
