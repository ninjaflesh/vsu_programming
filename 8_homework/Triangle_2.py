def is_triangle(a, b, c):
  min, middle, max = sorted([a, b, c])
  return (min + middle) > max


print(is_triangle(3, 3, 3))
print(is_triangle(5, 2, 2))
