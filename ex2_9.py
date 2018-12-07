s = str(input())
alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
c = int(input())
dir = str(input())
n = len(alpha)


point = ""
i = 0
for x in range(n):
    if s == alpha[x]:
        i = x
        if dir == "right":
            point = alpha[(i + c) % 26]
        else:
            point = alpha[(i - c) % 26]
print(point)
