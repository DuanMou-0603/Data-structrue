import time

# 通用计时装饰器
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()  # 高精度计时
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} 执行耗时：{end - start:.6f} 秒")
        return result
    return wrapper

# 测试 max() 函数 vs 遍历找最大值
@time_it
def find_max_loop(lst):
    """遍历找最大值（O(n)）"""
    if not lst:
        return None
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

@time_it
def find_max_builtin(lst):
    """内置max函数（O(n)，但底层优化）"""
    return max(lst)

# 冒泡排序优化前后对比
@time_it
def bubble_sort_original(lst):
    """原始冒泡排序（O(n²)）"""
    lst_copy = lst.copy()
    n = len(lst_copy)
    for i in range(n):
        for j in range(n - i - 1):
            if lst_copy[j] > lst_copy[j+1]:
                lst_copy[j], lst_copy[j+1] = lst_copy[j+1], lst_copy[j]
    return lst_copy

@time_it
def bubble_sort_optimized(lst):
    """优化冒泡排序（提前退出，仍O(n²)但实际更快）"""
    lst_copy = lst.copy()
    n = len(lst_copy)
    for i in range(n):
        swapped = False  # 标志位：是否发生交换
        for j in range(n - i - 1):
            if lst_copy[j] > lst_copy[j+1]:
                lst_copy[j], lst_copy[j+1] = lst_copy[j+1], lst_copy[j]
                swapped = True
        if not swapped:  # 无交换则列表已有序，提前退出
            break
    return lst_copy

# 测试调用
if __name__ == "__main__":

    # 测试找最大值
    test_lst = [i for i in range(100000)]
    find_max_loop(test_lst)
    find_max_builtin(test_lst)

    # 测试冒泡排序优化
    reverse_lst = [i for i in range(10000, 0, -1)]  # 逆序列表（对抗数据）
    bubble_sort_original(reverse_lst)
    bubble_sort_optimized(reverse_lst)