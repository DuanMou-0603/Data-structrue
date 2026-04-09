# 串基础信息
s = "abcdefgh"
print("原串：", s)
print("长度：", len(s))       # 8
print("子串[1:4]：", s[1:4])  # bcd
print("拼接：", s + "xyz")    # abcdefghxyz
print("'cd' 是否存在：", "cd" in s)  # True
print("查找'ef'位置：", s.find("ef")) # 4