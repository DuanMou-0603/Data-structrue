# 示例：1到n求和的两种实现（O(n) vs O(1)）
def sum_n_loop(n):
    """O(n)：循环累加"""
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def sum_n_formula(n):
    """O(1)：公式计算"""
    return n * (n + 1) // 2

# 时间复杂度示例
# 示例1：O(1) 常数时间
def constant_time_demo():
    lst = [1, 2, 3, 4, 5]
    return lst[2]  # 索引取值，不随列表长度变化

# 示例2：O(n) 线性时间
def linear_time_demo(n):
    total = 0
    for i in range(n):  # 循环n次
        total += i
    return total

# 示例3：O(log n) 对数时间
# 二分查找示例
def binary_search_demo(lst, target):
    left, right = 0, len(lst) - 1
    count = 0
    while left <= right:
        count = count + 1
        print(count)
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 示例 4: O(n log n) 线性对数时间
# 归并排序示例
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# 示例 5：O(n²) 平方时间
def square_time_demo(n):
    count = 0
    for i in range(n):  # 外层循环n次
        for j in range(n):  # 内层循环n次
            count += 1
    return count

# 示例 6：O(n^3) 立方时间
def cube_time_demo(n):
    count = 0
    for i in range(n):  # 外层循环n次
        for j in range(n):  # 内层循环n次
            for k in range(n):  # 内层循环n次
                count += 1
    return count

# 示例 7 ：O(n!) 阶乘时间（递归全排列）
def generate_permutations(lst):
    # 递归终止条件
    if len(lst) == 0:
        return [[]]
    permutations = []
    seen = set()  # 用于记录已经处理过的元素，避免重复
    for i in range(len(lst)):
        first = lst[i]
        # 跳过重复元素
        if first in seen:
            continue
        seen.add(first)
        remaining = lst[:i] + lst[i+1:]
        for p in generate_permutations(remaining):
            permutations.append([first] + p)
    return permutations

# 空间复杂度示例

# 示例 1：O(1) 常数空间
def constant_space_demo():
    a = 100
    b = 200
    return a + b  # 只使用了固定数量的变量，不随输入变化

# 示例 2：O(n) 线性空间
def linear_space_demo(n):
    lst = []
    for i in range(n):  # 循环n次，每次添加一个元素
        lst.append(i)
    return lst

# 示例 3：O(n^2) 平方空间
def square_space_demo(n):
    matrix = []
    for i in range(n):  # 外层循环n次
        row = []
        for j in range(n):  # 内层循环n次
            row.append(i * n + j)
        matrix.append(row)
    return matrix


# 测试调用
if __name__ == "__main__":
    # 示例：1到n求和的两种实现（O(n) vs O(1)）
    print("sum_n_loop(100)：", sum_n_loop(500))
    print("sum_n_formula(100)：", sum_n_formula(500))

    #时间复杂度
    # 示例 1：O(1) 常数时间
    print("O(1) 结果：", constant_time_demo())
    # 示例 2：O(n) 线性时间
    print("O(n) 结果（n=100）：", linear_time_demo(100))
    # 示例 3：O(log n) 对数时间
    print("O(log n) 结果（n=10）：", binary_search_demo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7))
    # 示例 4: O(n log n) 线性对数时间
    arr = [12, 11, 13, 5, 6, 7]
    print("排序前：", arr)
    merge_sort(arr)
    print("排序后：", arr)
    # 示例 5：O(n²) 平方时间
    print("O(n²) 结果（n=5）：", square_time_demo(5))
    # 示例 6：O(n^3) 立方时间
    print("O(n^3) 结果（n=5）：", cube_time_demo(5))
    # 示例 7：O(n!) 阶乘时间（递归全排列）
    print("O(n!) 结果（n=3）：", len(generate_permutations([1, 2, 3])))

    #空间复杂度
    # 示例 1：O(1) 常数空间
    print("O(1) 结果：", constant_space_demo())
    # 示例 2：O(n) 线性空间
    print("O(n) 结果（n=10）：", linear_space_demo(10))
    # 示例 3：O(n^2) 平方空间
    print("O(n^2) 结果（n=5）：", square_space_demo(5))

