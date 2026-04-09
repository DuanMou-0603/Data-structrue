# 构建 next 数组（LPS）
def build_next(p: str) -> list:
    m = len(p)
    next_arr = [0] * m
    j = 0  # 当前最长匹配长度
    print("构建next数组的过程：")
    print(f"模式串: {p}")
    for i in range(1, m):
        print(f"i={i}, p[i]='{p[i]}', 当前j={j}")
        # 不匹配则回退
        while j > 0 and p[i] != p[j]:
            print(f"  不匹配，回退j到next_arr[{j-1}]={next_arr[j-1]}")
            j = next_arr[j - 1]
        # 匹配则长度+1
        if p[i] == p[j]:
            print(f"  匹配，j+1={j+1}")
            j += 1
        next_arr[i] = j
        print(f"  next_arr[{i}] = {j}")
    print(f"最终next数组: {next_arr}")
    return next_arr

def kmp_match(s: str, p: str, next_arr: list) -> int:
    n, m = len(s), len(p)
    j = 0
    print("\nKMP匹配过程：")
    print(f"主串: {s}")
    print(f"模式: {p}")
    for i in range(n):
        print(f"\ni={i}, s[i]='{s[i]}', 当前j={j}")
        # 不匹配：回退模式串
        while j > 0 and s[i] != p[j]:
            print(f"  不匹配，回退j到next_arr[{j-1}]={next_arr[j-1]}")
            j = next_arr[j - 1]
        if s[i] == p[j]:
            print(f"  匹配，j+1={j+1}")
            j += 1
        # 显示当前匹配状态
        print(f"  当前匹配窗口: {s[i-j+1:i+1] if j > 0 else ''}")
        # 匹配成功
        if j == m:
            print(f"  匹配成功，返回位置 {i - m + 1}")
            return i - m + 1
    print("  匹配失败")
    return -1

# 调用演示
s = "ABABABCABABABD"
p = "ABABD"

next_arr = build_next(p)
print(kmp_match(s, p, next_arr))