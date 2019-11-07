# andrei_shvedau
# var 5

'''
 You are given n words. Some words may repeat. For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.
'''
# works only for unic unput
# map(lambda str: lst.count(str), lst)


def order():
    n = int(input())
    inp = dict()

    for i in range(n):
        st = input()

        if st not in inp.keys():
            inp[st] = 1
        else:
            inp[st] += 1

    print(len(inp.keys()))
    print(" ".join(str(i) for i in inp.values()))


if __name__ == '__main__':
    order()
