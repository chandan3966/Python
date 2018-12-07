s = str(input())
n = len(s)
k = list(s)
sub = ""
for x in range(1,n):
 if k[x] == k[0]:
  k[x] = "$"
for x in k:
 sub += x
print(sub)
