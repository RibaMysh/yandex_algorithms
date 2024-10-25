a, b, c = map(int, input().split())
print("WIN" if a % 2 == b % 2 and b % 2 == c % 2 else "FAIL")
