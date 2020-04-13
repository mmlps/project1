from os import system as sys
from time import sleep
scale=45
for i in range(scale+1):
    aaa = '='*i
    bbb = ' '*(scale-i)
    ccc =(i/scale)*10
    print("load message")
    print("\r{:^3.0f}%[{}[]{}]".format(ccc,aaa,bbb),end='')
    sleep(0.2)
    sys("cls")
