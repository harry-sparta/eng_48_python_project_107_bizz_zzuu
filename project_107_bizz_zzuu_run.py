from project_107_bizz_zzuu_functions import *

# Bizzuu run file
#

# ----------------------------------------------------------------------------------
# Run 1. user_input single response Bizzuu game:
# Comment out lines 14-22 before executing Run 1.
print(bizzuu(input('Enter a number:    ')))

# ----------------------------------------------------------------------------------
# Run 2. user_input determines range and speed for the program to iterate Bizzuu game up to:
# Comment out line 8 before executing Run 2.
import time

user_input = int(input('Enter a range:    ').strip())
user_input_time = float(input('Enter programe reponse time in (0.00 seconds):    ').strip())

for num in range(0, user_input):
    print(num)
    time.sleep(user_input_time)
    print(bizzuu(num))