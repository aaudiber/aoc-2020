with open('1.txt') as f:
  lines = f.read().split()

nums = [int(i) for i in lines]

for i in range(0, len(nums)):
  for j in range(i+1, len(nums)):
    if nums[i] + nums[j] == 2020:
      print(nums[i]*nums[j])


