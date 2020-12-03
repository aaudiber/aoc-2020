with open('2.txt') as f:
  lines = f.read().strip().split('\n')

valids = 0
for line in lines:
  r, c, p = line.split(' ')
  start, end = [int(i) for i in r.split('-')]
  c = c[0]
  count = 0
  for ch in p:
    if ch == c:
      count += 1
  if count >= start and count <= end:
    valids += 1 
  
print(valids)
