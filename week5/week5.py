def merge_sort_modify(arr):
    """
    基于分治思想的归并排序，同时统计相邻重复元素的总对数。

    返回: (排序后的数组, 相邻重复元素的总对数)
    """
    # 1. 拆分与基础情况 (Divide & Base Case)
    # 如果数组只有0个或1个元素，它本身是有序的，且不可能有重复对数
    if len(arr) <= 1:
        return arr, 0

    # 寻找中点进行拆分
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 2. 治理 (Conquer)
    # 递归调用，分别获取左右两半排好序的数组，以及它们内部本身的重复对数
    sorted_left, left_dups = merge_sort_modify(left_half)
    sorted_right, right_dups = merge_sort_modify(right_half)

    # 3. 合并 (Merge)
    merged = []
    i = j = 0
    cross_dups = 0  # 记录本次合并产生的新（跨界）重复对数
    last_shared = None

    # 使用双指针合并两个有序数组
    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] == sorted_right[j]:
            # 当左右指针指向的元素相同时，说明两个有序区间有交集，合并后必然首尾相连产生1对新的重复。
            if sorted_left[i] != last_shared:
                cross_dups += 1
                last_shared = sorted_left[i]

            merged.append(sorted_left[i])
            i += 1
        elif sorted_left[i] < sorted_right[j]:
            merged.append(sorted_left[i])
            i += 1
        else:
            merged.append(sorted_right[j])
            j += 1

    # 追加剩余元素
    merged.extend(sorted_left[i:])
    merged.extend(sorted_right[j:])

    # 4. 汇总
    # 核心分治逻辑：整体结果 = 左子树结果 + 右子树结果 + 合并时跨界产生的新结果
    total_dups = left_dups + right_dups + cross_dups

    return merged, total_dups


# ==========================================
# 测试代码
# ==========================================
if __name__ == "__main__":
    test_cases = [
        ([3, 2, 3, 2, 3], "常规乱序有重复"),  # 排序后:[2,2,3,3,3], 对数: 3 -> (2,2), (3,3), (3,3)
        ([1, 2, 3, 4, 5], "无重复元素"),  # 排序后:[1,2,3,4,5], 对数: 0
        ([7, 7, 7, 7], "全部重复"),  # 排序后:[7,7,7,7],   对数: 3
        ([5, 1, 5, 1, 5, 1], "交叉重复"),  # 排序后:[1,1,1,5,5,5], 对数: 4
        ([], "空数组"),  # 排序后:[],对数:0
    ]

    for arr, desc in test_cases:
        original_arr = arr.copy()
        sorted_arr, dup_count = merge_sort_modify(arr)
        print(f"[{desc}]")
        print(f"原数组: {original_arr}")
        print(f"排序后: {sorted_arr}")
        print(f"相邻重复对数: {dup_count}")
        print("-" * 30)