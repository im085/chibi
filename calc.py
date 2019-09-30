import re

def calc(s):
    n = 0
    nums = re.split('\d+', s)
    symb = re.split('[+*]', s)
    
    return sum(nums)

print(calc("1+2+3"))