import time
import random


def bubble_sort(arr):
    """冒泡排序 O(n²)"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def merge_sort(arr):
    """归并排序 O(n log n)"""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 合并两个有序数组
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def measure_time(func, data):
    start_time = time.perf_counter()
    result = func(data.copy())
    end_time = time.perf_counter()
    return result, end_time - start_time


# 测试不同规模
sizes = [10, 100, 1000, 10000, 100000]
print("算法性能对比测试：")
print("=" * 80)
print(f"{'n':>6} {'冒泡排序耗时(s)':>15} {'归并排序耗时(s)':>15} {'性能差距':>12} {'预测比率':>12}")

for n in sizes:
    # 生成随机数据
    data = [random.randint(1, 10000) for _ in range(n)]

    # 冒泡排序（只在小规模测试，避免等待太久）
    if n <= 10000:  # 限制冒泡排序的测试规模
        _, bubble_time = measure_time(bubble_sort, data)
    else:
        bubble_time = float('inf')  # 表示不实际运行

    # 归并排序
    _, merge_time = measure_time(merge_sort, data)

    if bubble_time != float('inf'):
        ratio = bubble_time / merge_time
        predicted_ratio = (n * n) / (n * (n.bit_length() - 1))  # 近似 n/log n
        print(f"{n:>6} {bubble_time:>15.6f} {merge_time:>15.6f} {ratio:>12.2f}x {predicted_ratio:>12.2f}")
    else:
        print(f"{n:>6} {'N/A (太慢)':>15} {merge_time:>15.6f} {'N/A':>12} {'N/A':>12}")

