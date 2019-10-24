# andrei_shvedau
# var 5

'''
Get most-common element of the list.
'''


def most_encout():

    n = int(input("List size: "))
    lst = []

    for i in range(0, n):
        lst.append(int(input()))

    print("")
    print(max(set(lst), key=lst.count))


if __name__ == '__main__':
    most_encout()
