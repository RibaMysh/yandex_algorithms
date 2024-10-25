x = int(input())
n1 = int(''.join(input().split()))
n2 = int(input())
print(*[x for x in str(n1 + n2)])