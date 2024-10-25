def generate_parentheses(n, s, left, right):
    if left == n and right == n:
        print(s)
        return
    if left < n:
        generate_parentheses(n, s + "(", left + 1, right)
    if right < left:
        generate_parentheses(n, s + ")", left, right + 1)


generate_parentheses(int(input()), "", 0, 0)
