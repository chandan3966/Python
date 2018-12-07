s1 = str(input())
s2 = str(input())
k1 = list(s1)
k2 = list(s2)
n1 = len(s1)
n2 = len(s2)

last1 = s1[n1-1]
last2 = s2[n2-1]

l1 = ""
l2 = ""
k1[n1-1] = last2
k2[n2-1] = last1

for x in k1:
 l1 += x
for x in k2:
 l2 += x
print(l1)
print(l2)
