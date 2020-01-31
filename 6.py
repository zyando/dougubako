N = int(input())

result = [0 for i in range(801)]

for i in range(N):
    f, l = list(map(int, input().split()))
    f -= 800
    l -= 800

    result = [result[i] + (1 if f <= i <= l else 0) for i in range(801)]

print(max(result))

900 1200
950 1100
1000 1050
1200 1250
1000 1700