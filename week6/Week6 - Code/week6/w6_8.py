# Sunday 算法

def sunday_match(s, p):
    n, m = len(s), len(p)
    if m == 0:
        return 0
    # 记录每个字符最后出现位置
    last = {}
    for i in range(m):
        last[p[i]] = i
    i = 0
    while i <= n - m:
        print(f"当前i={i}, 窗口: {s[i:i+m]}, 模式: {p}")
        j = 0
        while j < m and s[i + j] == p[j]:
            print(f"  对比 s[{i+j}]='{s[i+j]}' 与 p[{j}]='{p[j]}'，匹配")
            j += 1
        if j == m:
            print(f"  匹配成功，返回位置 {i}")
            return i
        if j < m:
            print(f"  对比 s[{i+j}]='{s[i+j]}' 与 p[{j}]='{p[j]}'，不匹配")
        # 关键：看对齐位的下一个字符
        if i + m >= n:
            break
        c = s[i + m]
        print(f"  下一个字符: s[{i+m}]='{c}'")
        shift = m - last.get(c, -1)
        print(f"  移动距离: {shift}")
        i += shift
        print(f"  新i={i}")
    return -1

# 调用演示
s = "ABABABCABABABD"
p = "ABABD"

print(sunday_match(s, p))