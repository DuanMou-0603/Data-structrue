import time
import random
import matplotlib.pyplot as plt
from functools import wraps


def timer_decorator(func):
    """非侵入式的计时装饰器"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        return result, execution_time

    return wrapper


@timer_decorator
def linear_search(arr, target):
    """O(n) 线性搜索算法"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


@timer_decorator
def binary_search(arr, target):
    """O(log n) 二分搜索算法（需要排序数组）"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


@timer_decorator
def bubble_sort(arr):
    """O(n^2) 冒泡排序算法"""
    n = len(arr)
    arr = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def generate_test_data(size, data_type="random"):
    if data_type == "random":
        return [random.randint(1, size * 2) for _ in range(size)]
    elif data_type == "sorted":
        return list(range(size))


def visualize_complexity():
    """可视化算法复杂度"""
    # 定义不同的输入规模
    sizes = [100, 500, 1000, 2000, 3000, 4000, 5000]

    print("开始基准测试...")

    # 测试线性搜索 O(n)
    linear_times = []
    for size in sizes:
        data = generate_test_data(size, "random")
        target_val = data[size // 2] if size > 0 else 0
        _, exec_time = linear_search(data, target_val)
        linear_times.append(exec_time)

    # 测试二分搜索 O(log n)
    binary_times = []
    for size in sizes:
        data = sorted(generate_test_data(size, "random"))  # 二分搜索需要排序数据
        target_val = data[size // 2] if size > 0 else 0
        _, exec_time = binary_search(data, target_val)
        binary_times.append(exec_time)

    # 冒泡排序O(n^2)
    bubble_sizes = [100, 200, 300, 400, 500, 600, 700]
    bubble_times = []
    for size in bubble_sizes:
        data = generate_test_data(size, "random")
        _, exec_time = bubble_sort(data)
        bubble_times.append(exec_time)

    # 创建可视化图表
    plt.figure(figsize=(14, 10))

    # 子图1：比较所有算法的时间复杂度
    plt.subplot(2, 2, 1)
    plt.plot(sizes, linear_times, 'b-o', label='Linear Search O(n)', linewidth=2)
    plt.plot(sizes, binary_times, 'g-s', label='Binary Search O(log n)', linewidth=2)
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Algorithm Complexity Comparison')
    plt.legend()
    plt.grid(True)

    # 子图2：单独显示冒泡排序 O(n^2)
    plt.subplot(2, 2, 2)
    plt.plot(bubble_sizes, bubble_times, 'r-^', label='Bubble Sort O(n²)', linewidth=2)
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Bubble Sort Complexity O(n²)')
    plt.legend()
    plt.grid(True)

    # 子图3：对数坐标下的复杂度比较
    plt.subplot(2, 2, 3)
    plt.loglog(sizes, linear_times, 'b-o', label='Linear Search O(n)', linewidth=2)
    plt.loglog(sizes, binary_times, 'g-s', label='Binary Search O(log n)', linewidth=2)
    plt.xlabel('Input Size (log scale)')
    plt.ylabel('Execution Time (log scale)')
    plt.title('Log-Log Plot of Algorithm Complexities')
    plt.legend()
    plt.grid(True)

    # 子图4：理论复杂度对比
    plt.subplot(2, 2, 4)
    # 归一化数据以便比较
    normalized_linear = [t / max(linear_times) for t in linear_times]
    normalized_binary = [t / max(binary_times) for t in binary_times]
    normalized_bubble = [t / max(bubble_times) for t in bubble_times[:len(normalized_linear)]]

    plt.plot(sizes, normalized_linear, 'b-o', label='Normalized Linear O(n)', linewidth=2)
    plt.plot(sizes, normalized_binary, 'g-s', label='Normalized Binary O(log n)', linewidth=2)
    plt.plot(sizes[:len(normalized_bubble)], normalized_bubble, 'r-^', label='Normalized Bubble O(n²)', linewidth=2)
    plt.xlabel('Input Size')
    plt.ylabel('Normalized Execution Time')
    plt.title('Normalized Algorithm Comparison')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()


    print("\n 性能测试结果摘要 ")
    print(f"{'Size':<10} {'Linear O(n)':<15} {'Binary O(log n)':<18} {'Bubble O(n²)':<15}")
    print("-" * 65)

    for i, size in enumerate(sizes):
        linear_time = f"{linear_times[i]:.6f}s" if i < len(linear_times) else "N/A"
        binary_time = f"{binary_times[i]:.6f}s" if i < len(binary_times) else "N/A"
        bubble_time = f"{bubble_times[i]:.6f}s" if i < len(bubble_times) else "N/A"

        print(f"{size:<10} {linear_time:<15} {binary_time:<18} {bubble_time:<15}")


if __name__ == "__main__":
    print("算法复杂度分析与可视化程序")
    print("本程序将演示三种不同时间复杂度的算法:")
    print("1. 线性搜索 - O(n)")
    print("2. 二分搜索 - O(log n)")
    print("3. 冒泡排序 - O(n²)")
    print()

    visualize_complexity()