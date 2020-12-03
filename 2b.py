with open('2.txt') as f:
  lines = f.read().strip().split('\n')

valids = 0
for line in lines:
  r, c, p = line.split(' ')
  start, end = [int(i) for i in r.split('-')]
  c = c[0]
  matches = 0
  if p[start-1] == c:
    matches += 1
  if p[end-1] == c:
    matches += 1

  if matches == 1:
    valids += 1
  
print(valids)
