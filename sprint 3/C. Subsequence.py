def find_subseq(seq, sub):
    ln, index = len(sub), 0
    for el in seq:
        if el == sub[index]:
            index += 1
            if index == ln:
                return True
    return False




sub = input()
seq = input()
print(find_subseq(seq, sub))