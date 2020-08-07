a, b, c = map(int, input().split())
x = 0
if b > c:
    print(-1)
else:
    while True:
        if x*c > a + x*b:
            print(x)
            break
        x += 1