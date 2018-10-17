#L = ["王大傻一号", "王大傻二号", "王大傻三号", "王大傻四号", '王大傻五号', '王大傻六号']

# print('L[0:3]= ', L[0:3])
# print('L[:3]=', L[:3])
# print('L[2:4]= ', L[2:4])
# print('L[-2:]=', L[-2:])
# print('L[-2:-1]=', L[-2:-1])
# print(L[2:5:2])
# print(L[::2])
# print(L[:])

def trim(s):
    ss = []
    for x in s:
        if x != ' ':
            #print(x)  
            ss.append(x)
    return ss

#print(trim(L[0]))
print(trim('    王大傻     '))


