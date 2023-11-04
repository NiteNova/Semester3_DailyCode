import random
nums = []
for i in range(30):
  nums.append(random.randrange(0, 50))
print("The randomized list:", nums)
print()

for j in range(len(nums)-1):
  smallest = nums[j]
  for i in range(len(nums)-j):
    if nums[i+j] < smallest:
      smallest = nums[i+j]
      toSwap = i+j
      
  temp = nums[j]
  nums[j] = smallest
  nums[toSwap] = temp
print("smallest is:", smallest)
print(nums)
