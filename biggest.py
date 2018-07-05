def bigger (a, b):
    if a>b:
        return a
    else:
        return b

def biggest (c, d, e):
    if c > bigger (d, e):
        return c
    else:
        return bigger(d, e)


print biggest(1, 2, 3)
print biggest(4, 6, 5)
print biggest(9, 8, 7)
print biggest(2, 1, 2)
