def myfunction(name):
   n = len(name)
   p = len(name[0])
   max = name[0]
   for x in range(1,n):
    if p < len(name[x]):
     p = len(name[x])
     max = name[x]
   return max


print("Enter the numberof strings:")
n = int(input())
s = ['']*n
for x in range(n):
 print("enter ",x+1," string:")
 s[x] = str(input())
print("Largest string:")
print(myfunction(s))
