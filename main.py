def greater10(x, y):
    if 10 - x < 10 - y:
        return x
    elif 10 - x > 10 - y:
        return y
    else:
        return 0

print(greater10(4,4))