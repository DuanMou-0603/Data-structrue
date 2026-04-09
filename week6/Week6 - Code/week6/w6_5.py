# 构建 next 数组（LPS）
def build_next(p: str) -> list:
    m = len(p)
    next_arr = [0] * m
    j = 0  # 当前最长匹配长度
    for i in range(1, m):
        # 不匹配则回退
        while j > 0 and p[i] != p[j]:
            j = next_arr[j - 1]
        # 匹配则长度+1
        if p[i] == p[j]:
            j += 1
        next_arr[i] = j
    return next_arr

# 调用演示
p = "ABABD"

next_arr = build_next(p)
print(next_arr)
