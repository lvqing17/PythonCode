import math
def quadratic(a, b, c):
    m = b * b - 4 * a * c
    if m >= 0 and a != 0:
       x1 = (-b + math.sqrt(m)) / (2 * a)
       x2 = (-b - math.sqrt(m)) / (2 * a)
       return x1, x2
    elif a == 0:
        x1 = x2 = -c / b
        return x1, x2
    else:
        return("错误")

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
