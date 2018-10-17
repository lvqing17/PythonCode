sum = 0
x = 1
while x < 101:
   print(x)
   #if x > 10:
    #    print(x)
   #    break
   sum = sum + x
   x = x + 1
   if x % 2 == 1:
      continue
   print(x)
print(sum)