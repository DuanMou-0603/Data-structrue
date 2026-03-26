def factorial(n):
    """递归计算阶乘"""
    print(f"计算 {n} 的阶乘")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    print(factorial(5))
    #print(factorial(1000)) # RecursionError: maximum recursion depth exceeded


