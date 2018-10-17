def product(*number):
    # //计算什么？
    sum = 1
    for n in number:
        sum *= n
    return sum
x = product(1,2,3)
print(x)

print(product(5,4))

def productw(number):
    sum = 1
    for m in number:
        sum *= m
    return sum

print(productw([5, 4]))    