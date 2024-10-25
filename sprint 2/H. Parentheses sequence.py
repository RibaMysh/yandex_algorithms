d = {'{': '}',
     '(': ')',
     '[': ']'}


def is_correct_bracket_seq(s):
    if s == "":
        return True
    stack = []

    for el in s:
        if el in d:
            stack.append(el)
        else:
            if len(stack) == 0 or el != d[stack[-1]]:
                return False
            else:
                stack.pop()
    return len(stack) == 0


print(is_correct_bracket_seq(input()))
