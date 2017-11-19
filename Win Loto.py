import random

nums = []

balls = [i for i in range(1,50)]
random.shuffle(balls)
nums = balls[:6]

print("Here are your 'lucky dip' numbers:")
print(nums)
print("Remember to split any winnings with me!")
