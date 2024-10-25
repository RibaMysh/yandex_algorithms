s1 = input()
s2 = input()
for x in s2:
    if x not in s1 or s1.count(x) != s2.count(x):
        print(x)
        break