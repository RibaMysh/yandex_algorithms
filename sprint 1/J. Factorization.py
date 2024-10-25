ans = []


def funk(n, ans=None):
    if ans is None:
        ans = []
    f = True
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            ans.append(i)
            funk(n // i, ans)
            f = False
            break
    if f:
        ans.append(n)
    return ans



print(*funk(int(input())))