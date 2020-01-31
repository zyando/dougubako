input()

d = list(map(int, input().split()))

n = []

for i in range(len(d)):
    count = 0
    for j in range(i, len(d) - 1):
        count += 1
        if d[j] <= d[j + 1]:
            break

    n.append(count)

print(max(n))