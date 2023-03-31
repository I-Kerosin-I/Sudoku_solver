from PIL import Image

colors = ((178, 179, 184), (172, 173, 176), (173, 173, 176), (107, 145, 214),
          (186, 193, 209))
pixel_cords = (((5, 3), 7), ((46, 4), 5), ((7, 71), 2), ((20, 52), 4),
               ((29, 19), 1), ((27, 29), 6), ((8, 50), 8), ((7, 27), 9),
               ((8, 15), 3))


def convert(img: Image):
    img = img.convert('RGB')
    if img.getpixel((35, 453)) == (0, 0, 0):  # no_score
        dy = 0
    elif img.getpixel((35, 486)) == (0, 0, 0):  # score
        dy = 33
    elif img.getpixel((35, 504)) == (0, 0, 0):  # battle
        dy = 51
    else:
        raise RuntimeError('Invalid board position')
    print(dy)
    img = img.crop((39, 457 + dy, 1044, 1462 + dy))
    # img.show()
    patterns = [img.crop((111 * x + 28 + (x // 3) * 3,
                          111 * y + 17 + (y // 3) * 3,
                          111 * x + 81 + (x // 3) * 3,
                          111 * y + 92 + (y // 3) * 3))
                for y in range(9) for x in range(9)]

    board, to_place = [], []
    for pattern in enumerate(patterns):
        for pixel in pixel_cords:
            if pattern[1].getpixel(pixel[0]) in colors:
                board.append(pixel[1])
                break
        else:
            board.append(0)
            to_place.append(pattern[0])

    return board, to_place, dy

# 7:   6 4   первый пиксел 1 1
# 5:   47 5   первый пиксел 1 1
# 2:   8 72   первый пиксел 1 1
# 4:   21 53   первый пиксел 1 1
# 1:   30 20   первый пиксел 1 1
# 6:   28 30   первый пиксел 1 1
# 8:   9 51   первый пиксел 1 1
# 9:   8 28   первый пиксел 1 1
# 3:   9 16   первый пиксел 1 1
