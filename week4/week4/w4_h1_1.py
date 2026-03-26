def recursive_function(n):
    if n != 0:
        return recursive_function(n - 1)
    else:
        return 0


try:
    # 递归深度超过最大限制
    # n = 996
    print("n = 996")
    recursive_function(996)
    # n = 1000
    print("n = 1000")
    recursive_function(1000)

except RecursionError as e:
    # 通常支持递归深度不到1000层
    print(f"崩溃: {e}")