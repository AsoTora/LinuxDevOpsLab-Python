# andrei_shvedau
# var 5


def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    tmp = list(i for i in range(10, 28))  # 10..27
    chars = dict(zip(tmp, [chr(c) for c in range(65, 81 + 1)]))  # A..Q

    while n:
        d = int(n % b)
        if d in tmp:
            digits.append(chars[d])
        else:
            digits.append(d)
        n //= b
    return digits[::-1]


def numberToBaseReverse(n, b):
    tmp = list(i for i in range(10, 28))  # 10..27
    chars = dict(zip([chr(c) for c in range(65, 81 + 1)], tmp))  # A..Q

    figures = []
    for i in str(n):
        print(chars.get(i, i))
        figures.append(int(chars.get(i, i)))
    figures = figures[::-1]

    result = 0
    for i in range(len(figures)):
        result += figures[i] * b ** i
    return result


def decode():
    inp = input()

    base = list(str(i) for i in range(10))  # 0..9
    for c in range(65, 81 + 1):  # 0..9 + A..Q
        base.append(chr(c))

    indeces = dict(zip([i for i in range(1, 28)], [chr(c) for c in range(97, 122 + 1)]))  # a..z
    indeces[27] = ' '

    mess = ""
    for i in range(len(inp)):
        mess += indeces.get((((base.index(inp[i]) - i - 1) % 27 + 27) % 27))
    print(mess)


if __name__ == '__main__':
    decode()
