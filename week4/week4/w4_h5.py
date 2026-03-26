def pause():
    """按回车继续下一步"""
    input("")


def fact(n, stack_trace):
    """
    递归计算阶乘，带调用栈追踪
    """
    # 压入调用栈
    stack_trace.append(f"fact({n})")

    print(f"当前调用栈（从底到顶）：[", end="")
    print(" -> ".join(stack_trace), end="")
    print("]")
    print(f"正在执行：fact({n})")
    pause()

    # 基线条件（递归终止）
    if n == 0 or n == 1:
        print(f"fact({n}) 满足基线条件，返回 1")
        # 弹栈
        stack_trace.pop()
        pause()
        return 1

    # 递归调用
    print(f"fact({n}) 需要计算 {n} * fact({n - 1})")
    result = n * fact(n - 1, stack_trace)

    # 弹栈并返回结果
    print(f"fact({n}) 计算完成，返回结果：{result}")
    stack_trace.pop()

    print(f"当前调用栈（从底到顶）：[", end="")
    print(" -> ".join(stack_trace), end="")
    print("]")
    pause()

    return result


if __name__ == "__main__":
    n = 5
    print(f"===== 递归调用栈模拟：fact({n}) 阶乘计算 =====")

    # 用列表模拟调用栈
    call_stack = []
    final = fact(n, call_stack)

    print(f"\n最终结果：fact({n}) = {final}")
