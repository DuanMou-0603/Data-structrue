import time
import random
import string

def naive_match(s: str, p: str) -> int:
    n, m = len(s), len(p)
    for i in range(n - m + 1):
        j = 0
        while j < m and s[i + j] == p[j]:
            j += 1
        if j == m:
            return i
    return -1

# 生成随机测试数据
def generate_test_data():
    # 生成50-100个字符的随机字符串
    s_length = random.randint(50, 100)
    s = ''.join(random.choices(string.ascii_lowercase, k=s_length))
    
    # 从字符串中随机选择一个长度为3-10的子串作为模式
    p_length = random.randint(3, min(10, s_length))
    start_idx = random.randint(0, s_length - p_length)
    p = s[start_idx:start_idx + p_length]
    
    return s, p

# 测试次数
test_count = 100000

# 累积执行时间
naive_total_time = 0
find_total_time = 0

# 验证结果一致性
results_consistent = True

print(f"开始执行 {test_count} 次测试...")

# 执行测试循环
for i in range(test_count):
    # 每次循环生成不同的测试数据
    s, p = generate_test_data()
    
    # 测试朴素匹配算法
    start = time.perf_counter()
    naive_result = naive_match(s, p)
    end = time.perf_counter()
    naive_total_time += (end - start)
    
    # 测试内置find方法
    start = time.perf_counter()
    find_result = s.find(p)
    end = time.perf_counter()
    find_total_time += (end - start)
    
    # 验证结果是否一致
    if naive_result != find_result:
        results_consistent = False
        print(f"测试 {i+1} 结果不一致: 朴素匹配={naive_result}, find={find_result}")
        print(f"字符串: {s}")
        print(f"模式: {p}")

# 计算平均执行时间
naive_avg_time = naive_total_time / test_count
find_avg_time = find_total_time / test_count

print(f"\n测试完成!")
print(f"总测试次数: {test_count}")
print(f"朴素匹配算法总耗时: {naive_total_time:.6f} 秒")
print(f"内置find方法总耗时: {find_total_time:.6f} 秒")
print(f"朴素匹配算法平均耗时: {naive_avg_time:.9f} 秒/次")
print(f"内置find方法平均耗时: {find_avg_time:.9f} 秒/次")
print(f"性能差异: {naive_avg_time / find_avg_time:.2f} 倍")
print(f"结果是否一致: {results_consistent}")