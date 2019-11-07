def is_palindrom1(s):
    return s[::] == s[::-1]


def is_palindrom2(s):
    if s[0] != s[-1]:
        return False
    if len(s) < 2:
        return True
    else:
        return is_palindrom2(s[1:-1])


str = input("Enter: ")
print(is_palindrom1(str))
print(is_palindrom2(str))

# print(is_palindrom1("aibohphobia"))
# print(is_palindrom2("aibohphobia"))