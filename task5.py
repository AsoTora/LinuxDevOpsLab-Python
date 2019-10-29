# andrei_shvedau
# var 5


def keybord():
    keys = "qwertyuiopasdfghjklzxcvbnm"

    for c in range(100):  # only 100 tries before collapse
        k = input()
        if k == 'm':
            print('q')
        else:
            print(keys[keys.find(k) + 1])


if __name__ == '__main__':
    keybord()
