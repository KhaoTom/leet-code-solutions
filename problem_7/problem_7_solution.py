MININT = -2147483648
MAXINT = 2147483647


def reverse_integer(x):
    if x < 0:
        rx = -int(str(abs(x))[::-1])
    else:
        rx = int(str(x)[::-1])
    if rx < MININT:
        return 0
    if rx > MAXINT:
        return 0
    return rx
