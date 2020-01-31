N = int(input())

result = [0 for i in range(801)]

for i in range(N):
    f, l = list(map(int, input().split()))
    f -= 900
    l -= 900

    result = [result[i] + (1 if f <= i <= l else 0) for i in range(801)]

print(max(result))