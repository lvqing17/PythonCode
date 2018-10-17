import math
def power(x, n):
  s = 1
  while n > 0:
      n = n - 1
      s = s * x
  return s

print("power(2, 3)= ", power(2, 3))

def add_end(L = []):
    L.append("王大傻")
    return L

print(add_end([2, 5, 0]))

def calc(number):
  sum = 0
  for n in number:
      sum = sum + n * n
  return sum

print(calc([1, 2, 3]))
     