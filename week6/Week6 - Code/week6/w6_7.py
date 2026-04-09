# BM 算法

def bm_match(s, p):
    n, m = len(s), len(p)
    if m == 0:
        return 0
    # 坏字符表：记录每个字符最后出现位置
    bad_char = {}
    for i in range(m):
        bad_char[p[i]] = i
    i = 0
    while i <= n - m:
        print(f"当前i={i}, 窗口: {s[i:i+m]}, 模式: {p}")
        print(f"  BM算法从右往左对比:")
        j = m - 1
        while j >= 0 and s[i + j] == p[j]:
            # 显示当前对比位置
            marker = ' ' * (j) + '↑'
            print(f"  对比 s[{i+j}]='{s[i+j]}' 与 p[{j}]='{p[j]}'，匹配")
            print(f"  模式串: {p}")
            print(f"  对比位置: {marker}")
            j -= 1
        if j < 0:
            print(f"  匹配成功，返回位置 {i}")
            return i  # 匹配成功
        if j >= 0:
            # 显示当前对比位置
            marker = ' ' * (j) + '↑'
            print(f"  对比 s[{i+j}]='{s[i+j]}' 与 p[{j}]='{p[j]}'，不匹配")
            print(f"  模式串: {p}")
            print(f"  对比位置: {marker}")
        # 坏字符规则滑动
        bc = bad_char.get(s[i + j], -1)
        slide = j - bc
        print(f"  坏字符: s[{i+j}]='{s[i+j]}', 在模式串中最后出现位置: {bc}")
        print(f"  计算滑动距离: j={j} - bc={bc} = {slide}")
        i += max(1, slide)
        print(f"  新i={i}")
        print("  " + "-" * 50)
    return -1

# 调用演示
s = "ABABABCABABABD"
p = "ABABD"

print(bm_match(s, p))