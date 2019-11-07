# andrei_shvedau
# var 5

'''
 Given a lower and upper number bound, output a list of every possible self dividing number,
including the bounds if possible.
'''


def check(i):
    num = [int(x) for x in str(i)]

    for n in num:
        if n == 0 or i % n != 0:
            return 0
    return 1


def selfDividingNumbers():
    left = int(input())
    right = int(input())
    ans = []

    for i in range(left, right + 1):
        if check(i):
            ans.append(i)

    print(ans)


if __name__ == '__main__':
    selfDividingNumbers()
