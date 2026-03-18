import time
import random
import matplotlib.pyplot as plt


# 复用计时装饰器
def time_it_avg(runs=100):  # 小规模n增加运行次数，提升精度
    def decorator(func):
        def wrapper(*args, **kwargs):
            total_time = 0.0
            for _ in range(runs):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                end = time.perf_counter()
                total_time += end - start
            avg_time = total_time / runs
            return result, avg_time

        return wrapper

    return decorator


# 1. O(n)算法：线性查找（找最大值）
@time_it_avg(runs=100)
def linear_find_max(lst):
    max_val = lst[0]
    for num in lst[1:]:
        if num > max_val:
            max_val = num
            # 模拟耗时操作（如打印）
            print("",end="")
    return max_val


# 2. O(n log n)算法：归并排序（取排序后的最后一个元素作为最大值）
@time_it_avg(runs=100)
def merge_sort_find_max(lst):
    # 归并排序核心
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

    def merge(left, right):
        res = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res.extend(left[i:])
        res.extend(right[j:])
        return res

    sorted_lst = merge_sort(lst)
    return sorted_lst[-1]

def use_chinese():
    import matplotlib
    matplotlib.rcParams["font.sans-serif"] = ["SimHei"]
    matplotlib.rcParams["font.family"] = "sans-serif"
    matplotlib.rcParams["axes.unicode_minus"] = False

# 测试不同n下的耗时对比
def test_small_n_performance():
    # 测试小规模n：10、100、1000、10000、100000（覆盖“较小n”范围）
    n_list = [10, 100, 1000, 10000, 100000]
    linear_times = []
    merge_times = []

    print("=== O(n)线性查找 vs O(n log n)归并排序（找最大值）耗时对比 ===")
    for n in n_list:
        data = list(range(n))

        # O(n)算法耗时
        _, linear_avg = linear_find_max(data)
        linear_times.append(linear_avg)

        # O(n log n)算法耗时
        _, merge_avg = merge_sort_find_max(data)
        merge_times.append(merge_avg)

        print(
            f"n={n} | O(n)耗时：{linear_avg:.8f}s | O(n log n)耗时：{merge_avg:.8f}s | O(n log n)/O(n) = {merge_avg / linear_avg:.2f}倍")

    # 可视化对比
    plt.figure(figsize=(10, 6))
    plt.plot(n_list, linear_times, marker='o', label="O(n) 线性查找最大值", color='green')
    plt.plot(n_list, merge_times, marker='s', label="O(n log n) 归并排序找最大值", color='orange')
    plt.axvline(x=10000, color='red', linestyle='--', label="临界点（n≈10000）")  # 不同硬件临界点不同
    plt.xlabel("输入规模 n")
    plt.ylabel("平均耗时（秒）")
    plt.title("小规模n下 O(n) vs O(n log n) 算法耗时对比")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


# 执行测试
if __name__ == "__main__":
    use_chinese()
    test_small_n_performance()