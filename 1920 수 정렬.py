def binary_search(a, x):
    start = 0
    end = len(a)-1
    while start <= end:
        mid = (start+end)//2
        if x == a[mid]:
            return 1
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a = sorted(a)
for i in range(m):
    print(binary_search(a,b[i]))