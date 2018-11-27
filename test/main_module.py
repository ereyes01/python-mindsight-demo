def spin(how_many):
    x = 1

    for i in range(how_many):
        y = i/x
        x = x + x * i * i * i * i
