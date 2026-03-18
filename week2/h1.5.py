import time

# O(n) 遍历列表
def traverse_list(n):
    """遍历指定长度的列表"""
    lst = list(range(n))
    total = 0
    for num in lst:
        total += num  # 遍历中的计算操作
    return total

# 测试不同输入规模
n_sizes = [100, 1000, 10000, 1000000, 10000000, 100000000]  # 小、中、大、超大规模
for n in n_sizes:
    start = time.perf_counter()
    traverse_list(n)
    end = time.perf_counter()
    print(f"输入规模n={n}，遍历耗时：{end - start:.6f} 秒")

print(f"1.线性遍历，所以耗时与输入规模n成正比")
print(f"2.但仍能观察到耗时增长趋势，即额外开销带来的耗时增加超过线性增长的速度")
