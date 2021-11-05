import random

n = int(input("Введите желаемую длинну списка: "))
nums = []
for i in range(n): 
    nums.append(random.randint(1, n))

def find_missing_nums(nums):
    a = []
    for i in range(1, n + 1):
        a.append(i)
    absent = []    
    for i in a:
        if i not in nums:
            absent.append(i)
    print(absent)

find_missing_nums(nums)