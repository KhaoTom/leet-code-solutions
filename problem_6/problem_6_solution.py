def convert_to_zigzag_text(s, rows):
    if rows == 1:
        return s

    zig = True
    y = 0
    ztext = ['' for _ in range(rows)]

    for c in s:
        ztext[y] += c
        if zig:
            if y + 1 >= rows:
                zig = False
                y -= 1
            else:
                y += 1
        else:
            if y == 0:
                zig = True
                y = 1
            else:
                y -= 1

    return ''.join(ztext)
