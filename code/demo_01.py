_author_ = 'lvqing'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('王大傻一号')
    elif len(args) == 2:
        print('王大傻二号')
    else:
        print('王大傻三号')

if __name__ == '_main_':
    test()