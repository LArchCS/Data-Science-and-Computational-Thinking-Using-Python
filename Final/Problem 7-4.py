res = []

n = 5

res = []
for i in range(n):
    x = i
    y = (i+1) % n
    res.append((x,y))

final = []
for i in range(n):
    c = i
    d = i+1
    final.append((c,d))


print res
print final