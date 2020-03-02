"""
乱序字符串 是指 一个字符串只是另一个字符串的重新排列
前提：字符串由26个小写字母集合组成，长度相同
比如：python  typhon
目的：写一个布尔函数（返回值是布尔值的函数）
      solutions1('abcd','dbca')

"""

# 检查第一个字符串是不是出现在第二个字符串中
# 复杂度 O（）
def solutions1(s1,s2):
    alist = list(s2)

    pos1 = 0       # 1
    flag = True    # 1

    while flag and pos1 < len(s1):            # n
        pos2 = 0
        found = False
        while pos2 < len(s2) and not found:    # n^2
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found :
            alist[pos2] = None
            pos1 = pos1 + 1
        else:
            flag = False

    return flag

# print(solutions1('abcd','dbca'))

# print(solutions1('pythoa','onhytp'))




# 计数和比较法    aaaaaabbbbcccccc       cccccccccaaaaaaaabbbbbbb
# 计算每个字母出现的次数

def solutions2(s1,s2):

    c1 = [0]*26  # 记录s1中字母出现的次数
    c2 = [0]*26  # 记录s2中字母出现的次数

    # ord() 返回的是字符在  ASCll中的数字

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1


    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1


    count = 0
    flag = True

    while count < 26 and flag:
        if c1[count] == c2[count]:
            count = count + 1
            
        else:
            flag = False
        
    return flag
# print(solutions2('aaabbbbbcccc','bbbbbccccaaa'))


# 排序和比较  : s1 s2 他们都是由完全相同的字符组成的
def solutions3(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    # 排序
    alist1.sort()
    alist2.sort()

    flag = True

    pos = 0
    while pos < len(s1) and flag:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            flag = False
    
    return flag

print(solutions3('aaaabbbbcccc','bbbbccccaaaa'))

print(solutions3('python','thonpy'))




























