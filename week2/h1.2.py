import time
import random


def linear_search_max(lst):
    """O(n) 线性查找最大值"""
    # 增加不必要的print操作，模拟实际场景中的额外操作
    if not lst:
        return None
    max_val = -1
    for num in lst:
        if num > max_val:
            max_val = num
            # 非必要操作，仅用于模拟额外计算
            print("",end="")
    return max_val


def merge_sort_max(lst):
    """O(n log n) 归并排序后取最大值"""

    def merge_sort(arr):
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

    sorted_arr = merge_sort(lst)
    return sorted_arr[-1]


def quick_sort_max(lst):
    """O(n log n) 快速排序后取最大值"""

    def quick_sort(arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return quick_sort(left) + middle + quick_sort(right)

    sorted_arr = quick_sort(lst)
    return sorted_arr[-1]


def measure_time(func, data):
    """测量函数执行时间"""
    start_time = time.perf_counter()
    result = func(data.copy())
    end_time = time.perf_counter()
    return result, end_time - start_time


# 测试小规模数据
small_sizes = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
print("\n小规模数据下 O(n) vs O(n log n) 性能对比：")
print("=" * 70)
print(f"{'n':>4} {'O(n)线性查找':>12} {'O(nlogn)归并':>14} {'O(nlogn)快排':>14} {'归并/线性':>10} {'快排/线性':>10}")

for n in small_sizes:
    # 生成对线性排序不利的数据（顺序，每个元素都大于前一个）
    data = list(range(n))

    # 测量线性查找最大值
    _, linear_time = measure_time(linear_search_max, data)

    # 测量归并排序后取最大值
    _, merge_time = measure_time(merge_sort_max, data)

    # 测量快速排序后取最大值
    _, quick_time = measure_time(quick_sort_max, data)

    # 计算比率
    merge_ratio = merge_time / linear_time if linear_time > 0 else 0
    quick_ratio = quick_time / linear_time if linear_time > 0 else 0

    print(
        f"{n:>4} {linear_time:>12.8f} {merge_time:>14.8f} {quick_time:>14.8f} {merge_ratio:>10.2f} {quick_ratio:>10.2f}")

print("\n结论：")
print("1. 当n较小时，O(n)算法，函数调用开销、递归开销等导致时间损失严重")
print("2. 随着n增大，O(n)算法的优势会逐渐显现")