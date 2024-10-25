def sq(n: int) -> bool:
    # :(
    for i in range(0, int(n ** (1 / 4)) + 2):
        if 4 ** i == n:
            return True
    return False


n = int(input())
print(sq(n))
