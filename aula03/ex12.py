from time import process_time_ns
import time


def countdown(n):
    while n>0:
        time.sleep(0.5)
        n-=1
        print(n)
    
a=int(input("Introduz um número: "))
print(a)
countdown(a)