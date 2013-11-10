def equal(num1,num2):
    if num1<num2:
        print 'too small'
        return True
    if num1>num2:
        print 'too big'
        return True
    if num1 == num2:
        print 'OK'
        return False
        
import random
num = random.randint(1,5)
print 'GO'
a='b'

while a:
    an=input(">")
    a=equal(an,num)