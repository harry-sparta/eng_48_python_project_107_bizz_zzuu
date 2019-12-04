# Game codes-------------------------------------------------------------------------------------
def bizz(num):
    return num%3

def zzuu(num):
    return num%5

import time
user_num = int(input('Give me a max number to stop at:    '))
for counter_num in range(0,user_num):
    time.sleep(0.1)
    print(counter_num)
    time.sleep(0.3)
    if bizz(counter_num) and zzuu(counter_num) == 0:
        print('BIZZZZZZUUUUUUUUUU!')
    elif zzuu(counter_num) == 0:
        print('ZZUUUUUUUUUUUUUUUU!')
    elif bizz(counter_num) == 0:
        print('BIZZZZZZZZZZZZZZZZ!')
    else:
        print('...........')
