n = int(input())

if n % 2 == 0:
    print("D")
else:
    for i in range(3, n // 3):
        if n % i == 0:
            print("D")
            break
    else:
        print("P")