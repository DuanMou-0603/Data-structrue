# 计数器：记录每个数字 n 被调用了多少次
fib_counter = {}


def fib(n):
    """递归计算斐波那契数列"""
    # 每次进入函数，计数 +1
    fib_counter[n] = fib_counter.get(n, 0) + 1

    # 递归终止条件
    if n == 0:
        return 0
    if n == 1:
        return 1

    # 两个递归（且大量重复计算）
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    # n=20，修改观察效果
    result = fib(20)

    # 输出最终统计
    print("\n===== 每个数字的调用次数 =====")
    for num in sorted(fib_counter.keys(), reverse=True):
        print(f"fib({num}) 执行了 {fib_counter[num]} 次")