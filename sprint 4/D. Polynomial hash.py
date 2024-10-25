def h(s, a, m):
    result = 0
    for i in range(len(s)):
        result = (result * a + ord(s[i])) % m

    return result

a = int(input())
m = int(input())
s = input()
print(h(s, a, m))
