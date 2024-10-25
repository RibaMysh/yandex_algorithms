n1 = input()
n2 = input()
mx = max(len(n1), len(n2))
n1 = n1.zfill(mx)
n2 = n2.zfill(mx)
n1 = n1[::-1]
n2 = n2[::-1]
res = ''
overflow = 0
for i in range(mx):
    val = int(n1[i]) + int(n2[i]) + overflow
    overflow = val // 2
    res += str(val % 2)

if overflow == 1:
    res += "1"

print(res[::-1])
