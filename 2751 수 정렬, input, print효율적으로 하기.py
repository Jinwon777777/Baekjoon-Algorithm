import sys
import pprint

n = int(input())

a = [int(sys.stdin.readline().replace('\n', '')) for i in range(n)]
a.sort()

print(*a, sep='\n')