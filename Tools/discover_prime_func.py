def primo(num):
    if num == 2:
        return True
    if num <= 1:
        return False
    if (num % 2) == 0:
        return False
    for n in range(3, (num - 1)):
        if (num % n) == 0:
            return False
    return True