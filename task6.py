# andrei_shvedau
# var 5

'''
 Рассмотрим работу простейшего шифра. Шифруемое сообщение состоит из английских букв, записанных в
нижнем регистре и символа пробела. Шифрование происходит посимвольно. Каждой букве ставим в
соответствие число: a – 1, b – 2, … , z – 26, ‘ ‘ – 27. Далее индекс символа
складывается с номером в сообщении по модулю 27, а результат сложения представляется в системе
счисления с основанием 27 (0, 1, …, Q в верхнем регистре).
 Необходимо написать дешифратор.

 В позиционной системе счисления с основанием 27 для записи любого числа используются цифры 0–9 и
буквы латинского алфавита A–Q.
 Пример: в системе с основанием 27 десятичное число 26 записывается как Q и 27 записывается как 10
'''


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

    base = list(str(i) for i in range(0, 10))  # 0..9
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
