def findMinAndMax(L):
    min = L[0]
    max = L[0]
    for x in  L:
        if x < min:
           min = x
        elif x > max:
           max = x
        else:
            pass
    return (min, max)

print(findMinAndMax([3,2,6,9]))
            