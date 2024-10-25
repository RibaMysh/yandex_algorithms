def horner_hash(s, a, m):

    result = 0
    for symbol in s:
        result = (result * a + ord(symbol)) % m
    return result


def generate_strings(length):

    from itertools import product
    import string

    chars = string.ascii_lowercase
    for comb in product(chars, repeat=length):
        yield ''.join(comb)


def find_collision(a, m, max_len):

    hashes = {}
    for length in range(1, max_len + 1):
        for s in generate_strings(length):
            h = horner_hash(s, a, m)
            if h in hashes:

                print(hashes[h])
                print(s)
                return
            hashes[h] = s



a = 1000
m = 123987123
max_len = 1000
find_collision(a, m, max_len)