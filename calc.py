import re

def calc(s):
    symb = re.split('\d+', s)
    nums = re.split('[+*]', s)
    nums = [int(j) for j in nums]

    print(nums)

    n = nums[0]
    k = 1

    for i in symb:
        if i == "+":
            n = n + nums[k]
            k = k + 1
        elif i == "*":
            n = n * nums[k]
            k = k + 1
        else:
            pass
 
    return n

print(calc("1+2+3*4"))