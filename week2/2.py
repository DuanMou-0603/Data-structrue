import time

def time_demo():
    time1 = time.time()
    print("启动时间：", time1)

    # run some code
    time.sleep(2)

    time2 = time.time()
    print("当前时间：", time2)

    print("耗时：", time2 - time1)

def time_demo2():
    time1 = time.perf_counter()
    print("启动时间：", time1)

    # run some code
    time.sleep(2)

    time2 = time.perf_counter()
    print("当前时间：", time2)

    print("耗时：", time2 - time1)

# 测试 O(n) vs O(n²)
def linear_func(n):
    time1 = time.perf_counter()
    total = 0
    for i in range(n):
        total += i
    time2 = time.perf_counter()
    print("O(n) 耗时：", time2 - time1)
    return total

def square_func(n):
    time1 = time.perf_counter()
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    time2 = time.perf_counter()
    print("O(n²) 耗时：", time2 - time1)
    return count

# 测试调用
if __name__ == "__main__":

    # 测试 time.time() 与 time.perf_counter() 区别
    time_demo()
    time_demo2()


    # 测试不同复杂度函数耗时
    n = 100
    linear_func(n)
    square_func(n)  # 耗时远大于线性函数

    n = 2000
    linear_func(n)
    square_func(n)  # 耗时远大于线性函数

    n = 19000
    linear_func(n)
    square_func(n)  # 耗时远大于线性函数
