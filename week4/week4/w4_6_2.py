# 不做要求，仅供了解递归调用栈的实现原理
import inspect
def factorial(n):
    # 获取当前调用栈的信息, 包含当前函数调用的行号, 文件名, 函数名, 参数等信息
    frame_info = inspect.currentframe()
    stack = inspect.getouterframes(frame_info)
    # 优化显示调用栈信息
    print("\n调用栈信息:")
    for i, frame in enumerate(stack):
        if i == 0:  # 当前函数帧
            print(f"  帧{i}: 函数={frame.function}, 行号={frame.lineno}")
        elif 'factorial' in frame.function:  # 递归调用帧
            print(f"  帧{i}: 函数={frame.function}, 行号={frame.lineno}")
        else:  # 其他帧（如主调函数）
            print(f"  帧{i}: 函数={frame.function}, 文件={frame.filename.split('/')[-1]}")
     # 打印调用栈深度和参数
    print(f"深度: {len(stack)-1}, 计算 factorial({n})")
    if n ==1:
        print("到达基线，返回 factorial(1) = 1")
        return 1
    result = n * factorial(n-1)
    print(f"完成 fact({n}) = {n} * factorial({n-1}) = {result}")
    return result

# 执行函数，观察调用栈变化 factorial(3)
factorial(3)