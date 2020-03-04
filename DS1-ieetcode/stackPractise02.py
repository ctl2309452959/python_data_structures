
'''

使用"除2" 算法，将输入的十进制转换为8位2进制的数字
'''
from pythonds.basic.stack import Stack

# 十进制转二进制
def divide2(desNumber):
    s = Stack()


    while desNumber > 0:
        rem = desNumber % 2
        s.push(rem)
        desNumber = desNumber // 2  # 整除

    binString = ""

    while not s.isEmpty():
        binString = binString + str(s.pop())
    
    return binString

"""print(divide2(233))"""


"""
十进制 转   八进制，十六进制

"""

def divideBase(desNumber,base):
    digits = '0123456789ABCDEF'

    s = Stack()

    while desNumber > 0:
        rem = desNumber % base
        s.push(rem)
        desNumber = desNumber // base  # 整除

    binString = ""

    while not s.isEmpty():
        binString = binString + digits[s.pop()]
    
    return binString

print(divideBase(233,2))
print(divideBase(233,8))
print(divideBase(233,16))
















































