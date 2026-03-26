def recursive_mess(n, depth=0):
    """
    多分支递归 + 多层判断
    """
    # depth 展示递归深度，无实际意义
    # 用缩进展示调用深度
    indent = "|  " * depth
    print(f"{indent}→ 进入 recursive_mess({n}) 深度={depth}")

    if n <= 0:
        print(f"{indent}✓ n<=0，返回 1")
        return 1

    # 分支1：偶数
    if n % 2 == 0:
        a = recursive_mess(n - 1, depth + 1)

        # 这里藏了一个二次递归！超级难追踪！
        b = recursive_mess(n // 2, depth + 1)

        res = a + b
        print(f"{indent}← 偶数分支返回: {res}")
        return res

    # 分支2：奇数
    else:
        x = recursive_mess(n - 2, depth + 1)
        y = recursive_mess(n - 3, depth + 1)
        res = x * y + 1
        print(f"{indent}← 奇数分支返回: {res}")
        return res


if __name__ == "__main__":
    # n=10，修改观察效果
    result = recursive_mess(10)
    print("\n最终结果:", result)