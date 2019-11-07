def self_dividing(n):
    for d in str(n):
        if d == '0' or n % int(d) > 0:
            return False
    return True
