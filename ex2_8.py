def reverse(st):
  st1 = ""
  for i in st:
    st1 = i + st1
  return st1

s = str(input())
n = len(s)
if n % 4 == 0:
 print(reverse(s))
