# # Bizzuu tests
from project_107_bizz_zzuu_functions import *

# T1.1) Testing if user_num is a multiple of 3 returns true
print('\nT1.1) If we input 6, a multiple of 3 we should get a True')
print(' Results:   ',bizz_calc(6))

# T1.2) Testing if user_num is not a multiple of 3 returns false
print('\nT1.2) If we input 8, a non-multiple of 3 we should get a False')
print(' Result:   ',bizz_calc(8))

# T2.1) Testing if user_num is a multiple of 5 returns true
print('\nT2.1) If we input 10, a multiple of 5 we should get a True')
print(' Result:   ',zzuu_calc(10) == 0)

# T2.2) Testing if user_num is not a multiple of 5 returns false
print('\nT2.2) If we input 11, a non-multiple of 3 we should get a False')
print(' Result:   ',zzuu_calc(11) == 0)

# T3.1) Testing if user_num is a multuple of 3 and 5 returns true
print('\nT3.1) If we input 15, a multiple of 3 and 5 we should get a True')
print(' Result:   ',bizzuu_calc(10) == 0)

# T3.2.1) Testing if user_num is not a multiple 3 or 5 returns false
print('\nT3.2.1) If we input 18, a non-multiple of 5 we should get a False')
print(' Result:   ',bizzuu_calc(11) == 0)

# T3.2.2) Testing if user_num is not a multiple 3 or 5 returns false
print('\nT3.2.2) If we input 20, a non-multiple of 3 we should get a False')
print(' Result:   ',bizzuu_calc(11) == 0)

# T4.1) Testing if the bizzuu() function returns the right string
print('\nT4.1) If we input 9, a multiple of 3 we should get a BIZZZZZZ')
print(' Result:   ',bizzuu(9) == 'BIZZZZZZ', ', ',bizzuu(9))

# T4.2) Testing if the bizzuu() function returns the right string
print('\nT4.2) If we input 20, a multiple of 5 we should get a ZZUUUUUU')
print(' Result:   ',bizzuu(20) == 'ZZUUUUUU', ', ',bizzuu(20))

# T4.3) Testing if the bizzuu() function returns the right string
print('\nT4.3) If we input 30, a multiple of 3 and 5 we should get a BIZZZUUU')
print(' Result:   ',bizzuu(30) == 'BIZZZUUU', ', ',bizzuu(30))
