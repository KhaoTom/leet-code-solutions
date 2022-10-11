def convert_to_zigzag_text(s, rows):
    zig = True
    y = 0
    ztext = ['' for _ in range(rows)]
    initial_zig_step = 0 if rows == 2 else -1
    for c in s:
        ztext[y] += c
        if zig:
            if y + 1 >= rows:
                zig = False
                y -= 1
            else:
                y += 1
        else:
            if y - 1 <= 0:
                zig = True
                y = 0
            else:
                y -= 1

    return ''.join(ztext)
