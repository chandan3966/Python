s = str(input())
n = len(s)
s1 = s[0:2]
s2 = s[n-2:n]
if n < 2:
 print("Empty String")
else:
 print(s1+s2)
