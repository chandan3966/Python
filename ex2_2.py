s = str(input())
d = {}
for x in s:
 keys = d.keys()
 if x in keys:
  d[x] += 1
 else:
  d[x] = 1
print(d)
