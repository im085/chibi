import re

def calc(s):
    symb = re.split('\d+', s)
    nums = re.split('[+*]', s)
    nums = [int(j) for j in nums]
    del symb[0]
    del symb[-1]
    i = 0

    for j in range(len(symb)):
        if symb[i] == "*":
           nums[i] = nums[i] * nums[i+1]
           del nums[i+1]
           del symb[i]
           i = i - 1
        i = i + 1
    return sum(nums)

print(calc("3+7*4"))