#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if(i >= 'a' and i <= 'z'):
            i = ord(i) - 32
            print(chr(i),end='')
        else:
            print(i,end='')
    print('\n')

uppercase("best")
uppercase("Best School 98 Battery street")