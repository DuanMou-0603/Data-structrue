from collections import deque
import time

# ======================
# 1. 递归版
# 功能：从队列头部依次取出元素处理
# ======================
def recursive_process(items):
    if not items:
        return 0
    # 头部删除（list 这里极慢）
    first = items.pop(0)
    return first + recursive_process(items)


# ======================
# 2. 迭代版
# ======================
def iterative_process(queue):
    total = 0
    while queue:
        # 头部删除（O(1)）
        total += queue.popleft()
    return total


# ======================
# 3. 性能对比：list vs deque
# 场景：万级别数据 + 频繁头部操作
# ======================
def performance_test():
    # 使用 100 时递归可以正常运行
    TEST_SIZE = 100_000  # 建议使用的10万数据（100万耗时过久）

    print("=" * 60)
    print(f"测试数据量：{TEST_SIZE:,} 个元素")
    print("头部插入 + 头部删除（工程常见场景）")
    print("=" * 60)

    # ----------------------
    # 【差】list 测试
    # ----------------------
    print("\n→ 测试 list：")
    lst = []

    # 头部插入（list 极慢：O(n)）
    t1 = time.perf_counter()
    for i in range(TEST_SIZE):
        lst.insert(0, i)
    t2 = time.perf_counter()
    print(f"头部插入耗时：{t2 - t1:.6f}s")

    # 递归处理（直接栈溢出！！！）
    try:
        t3 = time.perf_counter()
        recursive_process(lst)
        t4 = time.perf_counter()
        print(f"递归处理耗时：{t4 - t3:.6f}s")
    except RecursionError:
        print("递归处理：失败！栈溢出（生产绝对禁用）")

    # 迭代 + list 头部删除（依然慢）
    t5 = time.perf_counter()
    total = 0
    # 构造一份完全相同的数据，保证结果一致
    lst = []
    for i in range(TEST_SIZE):
        lst.insert(0, i)

    while lst:
        total += lst.pop(0)
    t6 = time.perf_counter()
    print(f"迭代+list 头部删除：{t6 - t5:.6f}s")

    # ----------------------
    # 使用deque 测试（工程标准）
    # ----------------------
    print("\n→ 测试 deque：")
    dq = deque()

    # 头部插入（O(1)）
    t1 = time.perf_counter()
    for i in range(TEST_SIZE):
        dq.appendleft(i)
    t2 = time.perf_counter()
    print(f"头部插入耗时：{t2 - t1:.6f}s")

    # 迭代 + deque 头部删除（O(1)）
    t3 = time.perf_counter()
    total2 = iterative_process(dq)
    t4 = time.perf_counter()
    print(f"迭代+deque 头部删除：{t4 - t3:.6f}s")

    print("\n最终结果检查，验证正确性")
    print(f"list 处理结果：{total}")
    print(f"deque 处理结果：{total2}")
    if total == total2:
        print("结果一致")
    else:
        print("结果不一致")
    print("=" * 60)


if __name__ == "__main__":
    performance_test()