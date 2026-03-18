import time

def my_func():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    """遍历找最大值（O(n)）"""
    if not lst:
        return None
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

# 手动跑 1000 次取平均
n = 100
start = time.time()

for _ in range(n):
    my_func()

total_time = time.time() - start
avg_time = total_time / n

print(f"总耗时：{total_time:.6f}")
print(f"平均耗时：{avg_time:.6f}")

if __name__ == "__main__":
    my_func()