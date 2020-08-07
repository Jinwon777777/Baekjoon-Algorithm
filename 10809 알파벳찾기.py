a = input()
alp = list(map(chr,range(97,123)))
ans = list(map(a.find,alp))
print(*ans, sep=' ')