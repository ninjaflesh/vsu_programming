def is_triangle(a, b, c):
    pol = (a + b + c) / 2.0
    s = (pol*(pol - a)*(pol - b)*(pol - c))
    return s > 0


is_triangle(3, 3, 3)
