def gener(digits, res):
    if len(digits) == 0:
        print(res, end=' ')
        return
    for letter in letters[digits[0]]:
        gener(digits[1:], res + letter)


digit = input()
letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

gener(digit, '')
