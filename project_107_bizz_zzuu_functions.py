# Game codes-------------------------------------------------------------------------------------
# 1.) A function to test/ validate if 'num' is multiple of 3
def bizz_calc(num):
    return num%3 == 0

# 2.) A function to test/ validate if 'num' is multiple of 5
def zzuu_calc(num):
    return num%5 == 0

# 3.) A function to test/ validate if 'num' is multiple of 5 and 3
def bizzuu_calc(num):
    return (bizz_calc(num) and zzuu_calc(num))

# 4.) A function to group (1. 2. and 3.) in a control flow block
def bizzuu(num):
    num_format = int(num)
    if bizzuu_calc(num_format):
        return 'BIZZZUUU'
    elif zzuu_calc(num_format):
        return 'ZZUUUUUU'
    elif bizz_calc(num_format):
        return 'BIZZZZZZ'
    else:
        return '........'
