from parse import *

with open('3.txt') as f:
  lines = f.read().strip().split('\n')

counts = []
for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
  count = 0
  x = 0
  for line in lines[0:len(lines):slope[1]]:
    if line[x % len(line)] == "#":
      count += 1
    x += slope[0]
  counts.append(count)
prod = 1
for count in counts:
  prod *= count

print(prod)
  


