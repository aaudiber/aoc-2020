from parse import *

with open('3.txt') as f:
  lines = f.read().strip().split('\n')

count = 0
x = 0
for line in lines:
  if line[x % len(line)] == "#":
    count += 1
  x += 3

print(count)
