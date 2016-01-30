#I need my glasses to see. View this video for info: https://www.youtube.com/watch?v=eZUa5k_VIZg,  short ans: n is prime if (n-1)! +1 = s where s is divisible by n.
import math
import sys

def devBy(n, s):
    if s % n == 0:
        return True
    else:
        return False

def factorial(n):
    return math.factorial(n)
def Prime(n):
    ans = factorial( (n-1) ) + 1
    if  devBy(n, ans):
        return True , ans/n
    else:
        return False, 0
def wilsonPrime(n):
    pr, ans = Prime(n)
    if pr:
        if devBy(n,ans):
            return True
        else:
            return False
    else:
        return False
def user():
    n = raw_input("Enter a number: ")
    try:
        n = int(n)
    except:
        print "You must enter a valid number"
        sys.exit(2)
    pr, ans = Prime(n)
    if pr:
        print "Your number is prime "
        if wilsonPrime(n):
            print "And it is a Wilson Prime"
        else:
            print "But it is not a Wilson Prime"
    else:
        print "Your number is not prime"
def automatic(starting_num):
    n = starting_num
    while True:
        if wilsonPrime(n):
            print n
            n += 1
        else:
            if n % 1000 == 0:
                print "not {}".format(n)
            n += 1

automatic(1)
