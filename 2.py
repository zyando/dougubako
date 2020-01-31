import math

N = int(input())

p = (0, 0)
d = 0

for i in range(N):
    x, y = list(map(int, input().split()))
    d += math.sqrt((x - p[0]) ** 2 + (y - p[1]) ** 2)
    p = (x, y)

print(d)

