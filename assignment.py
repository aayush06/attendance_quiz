# In a university, your attendance determines whether you will be allowed to 
# attend your graduation ceremony. 
# You are not allowed to miss classes for four or more consecutive days. 
# Your graduation ceremony is on the last day of the academic year, which is the Nth day.

# Your task is to determine the following:

# 1. The number of ways to attend classes over N days.
# 2. The probability that you will miss your graduation ceremony.


from functools import lru_cache
from math import gcd

@lru_cache(None)
def calculate(no_of_days=None, prev=2):
    if no_of_days == 0:
        return 1
    ans = 0
    if prev == 1:
        ans += calculate(no_of_days-1, 1) + calculate(no_of_days-1, 0)
    elif prev == 0:
        ans += calculate(no_of_days-1, 1)
    else:
        ans += calculate(no_of_days-1, 1) + calculate(no_of_days-1, 0)
    return ans


no_of_days = int(input("Enter no. of days"))

calculate = [[0] * no_of_days for _ in range(2)]
calculate[0][0], calculate[1][0] = 1, 1

for i in range(1, no_of_days):
    calculate[1][i] = calculate[1][i-1] + calculate[0][i-1]
    calculate[0][i] = calculate[1][i-1]

present, absent = calculate[1][-1], calculate[0][-1]
total = present + absent

print(total)
g = gcd(absent, total)

absent //= g
present //= g

print('{}/{}'.format(absent, total))
