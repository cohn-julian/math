import sys
import timeit
sys.setrecursionlimit(999999999)
cach = {1:True}
def cconjecture(int):
    if cach.get(int) == None: #not in cach
        if (int & 0x1): #faster way of checking if # is odd
            return cconjecture(int*3 + 1)
        else:
            return cconjecture(int/2)
    else:
        return True
def main():
    start = timeit.default_timer()
    num = 1
    while cconjecture(num):
                    cach[num] = True
                    num += 1
                    if (num % 1000000) == 0:
                            stop = timeit.default_timer()
                            print num
                            print  (stop - start)/1000000
                            start = timeit.default_timer()
main()
