import time
import random


def bubble_sort(arr):
    """原始冒泡排序 O(n²)"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def optimized_bubble_sort(arr):
    """优化冒泡排序 O(n²)，但常数因子更小"""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # 如果没有交换，说明已排序完成
    return arr


def measure_time(func, data):
    """测量函数执行时间"""
    start_time = time.perf_counter()
    result = func(data.copy())
    end_time = time.perf_counter()
    return result, end_time - start_time


# 测试不同规模的数据
sizes = [100, 1000, 10000, 100000]
print("冒泡排序在不同规模下的耗时对比：")
print("=" * 60)

for n in sizes:
    # 生成随机数据
    data = [random.randint(1, 1000) for _ in range(n)]

    # 测试原始冒泡排序
    _, time_taken = measure_time(bubble_sort, data)
    print(f"n={n:>6}: 原始冒泡排序耗时 {time_taken:>8.6f} 秒")

    if n == 100:
        base_time = time_taken
    else:
        ratio = time_taken / base_time
        print(f"      -> 相对于n=100的耗时倍数: {ratio:>8.2f}")

    # 测试优化冒泡排序
    _, opt_time_taken = measure_time(optimized_bubble_sort, data)
    print(f"n={n:>6}: 优化冒泡排序耗时 {opt_time_taken:>8.6f} 秒")

    if n == 100:
        base_time = opt_time_taken
    else:
        ratio = opt_time_taken / base_time
        print(f"      -> 相对于n=100的耗时倍数: {ratio:>8.2f}")

    print("-" * 40)