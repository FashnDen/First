from fnmatch import *
# for x in range(253, 10**8, 253):
#     if fnmatch(str(x), '12??15*6'):
#         print(x, x//253)
for x in range(237,10**8,237):
    if fnmatch(str(x), '81?2*80') and not fnmatch(str(x), '*9*'):
        print(x, x//237)