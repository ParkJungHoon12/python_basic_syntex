import math
import statistics


def collatz(number, option):    
    count = 1
    MAX_NUMBER = number

    while number > 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1

        count = count + 1

        if(MAX_NUMBER < number):
            MAX_NUMBER = number
  
    # option == 1 : return count
    # option == 2 : return MAX_NUMBER

    if option == 1:
        return count
    elif option == 2:
        return MAX_NUMBER


def MAX_collatz(a, b):
    LENGTH = []
    MAXNUM = []

    for i in range(a, b+1):
        LENGTH.append(collatz(i,1))
        MAXNUM.append(collatz(i,2))

    print("%d to %d, MAX_LENGTH : %d, MAX_COUNT : %d, userrate = %f" 
          % (a, b, max(LENGTH), max(MAXNUM), 100*statistics.median(LENGTH)/math.log(statistics.median(MAXNUM)) ))
    
for i in range(10000):    
    MAX_collatz(i*10000000000000000000000, i*10000000000000000000000 + 9999)
