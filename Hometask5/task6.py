# andrei_shvedau
# var 5


def decode(inp):

    base = list(str(i) for i in range(10))  # 0..9
    for c in range(65, 81 + 1):  # 0..9 + A..Q
        base.append(chr(c))

    indeces = dict(zip([i for i in range(1, 28)], [chr(c) for c in range(97, 122 + 1)]))  # a..z
    indeces[0] = ' '

    mess = ""
    for i in range(len(inp)):
        mess += indeces.get((((base.index(inp[i]) - i - 1) % 27 + 27) % 27))
    return str(mess)
