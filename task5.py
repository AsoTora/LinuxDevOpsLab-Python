# andrei_shvedau
# var 5

'''
 Для данной буквы английского алфавита нужно вывести справа стоящую букву на стандартной клавиатуре.
 При этом клавиатура замкнута, т.е. справа от буквы «p» стоит буква «a», от буквы «l» стоит
буква «z», а от буквы «m» — буква «q».
'''


def keybord():
    keys = "qwertyuiopasdfghjklzxcvbnm"

    c = 0
    while(True):
        k = input()
        if k == 'm':
            print('q')
        else:
            print(keys[keys.find(k) + 1])

        c += 1  # in original task we get a strict input from a file.
        if c == 100:
            break


if __name__ == '__main__':
    keybord()
