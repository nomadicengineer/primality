#!/usr/bin/python
import math

# Python program to ask the user for a range and display all the prime numbers in that interval

# take input from the user
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
class bcolors:
    PRIME = '\033[92m'
    OTHER = '\033[91m'
    ENDC = '\033[0m'
prime = []
allnum = []
for num in range(lower,upper + 1):
    allnum.append(num)
    if num >= 1:
        if num == 1:
            prime.append(num)
            continue
        if num == 2:
            prime.append(num)
            continue
        if num == 3:
            prime.append(num)
            continue
        if num == 5:
            prime.append(num)
            continue
        if (num % 2) == 0:
            continue
        if (num % 3) == 0:
            continue
        if (num % 5) == 0:
            continue
        for i in range(6,int(math.sqrt(num))+1):
            if (num % i) == 0:
                break
        else:
            prime.append(num)
for idx, n in enumerate(allnum):
    if n in prime:
        print bcolors.PRIME + "{:10d}".format(n)+ bcolors.ENDC,
    else:
        print bcolors.OTHER + "{:10d}".format(n)+ bcolors.ENDC,
    if (idx +1) %10 == 0:
            print
