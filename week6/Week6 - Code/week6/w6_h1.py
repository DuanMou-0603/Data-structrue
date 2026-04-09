# 多模式匹配下 KMP 衰减严重
import time

# 构建 next 数组（LPS）
def build_next(p: str) -> list:
    m = len(p)
    next_arr = [0] * m
    j = 0  # 当前最长匹配长度
    for i in range(1, m):
        while j > 0 and p[i] != p[j]:
            j = next_arr[j - 1]
        if p[i] == p[j]:
            j += 1
        next_arr[i] = j
    return next_arr

# KMP 单模式匹配
def kmp_match(s: str, p: str, next_arr: list) -> list:
    n, m = len(s), len(p)
    j = 0
    matches = []
    for i in range(n):
        while j > 0 and s[i] != p[j]:
            j = next_arr[j - 1]
        if s[i] == p[j]:
            j += 1
        if j == m:
            matches.append(i - m + 1)
            j = next_arr[j - 1]  # 继续寻找下一个匹配
    return matches

# 基于 KMP 的多模式匹配
def kmp_multi_pattern(s: str, patterns: list) -> dict:
    results = {}
    for pattern in patterns:
        next_arr = build_next(pattern)
        results[pattern] = kmp_match(s, pattern, next_arr)
    return results

# Aho-Corasick 算法实现
class TrieNode:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.patterns = []

class AhoCorasick:
    def __init__(self, patterns):
        self.root = TrieNode()
        self.build_trie(patterns)
        self.build_fail()
    
    def build_trie(self, patterns):
        for pattern in patterns:
            node = self.root
            for char in pattern:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.patterns.append(pattern)
    
    def build_fail(self):
        from collections import deque
        queue = deque()
        
        # 初始化根节点的子节点
        for char, node in self.root.children.items():
            node.fail = self.root
            queue.append(node)
        
        # BFS 构建失败指针
        while queue:
            current = queue.popleft()
            
            for char, child in current.children.items():
                # 找到失败指针
                fail_node = current.fail
                while fail_node and char not in fail_node.children:
                    fail_node = fail_node.fail
                
                if fail_node:
                    child.fail = fail_node.children[char]
                else:
                    child.fail = self.root
                
                # 合并模式串
                child.patterns.extend(child.fail.patterns)
                queue.append(child)
    
    def search(self, text):
        results = {}
        current = self.root
        
        for i, char in enumerate(text):
            # 沿着失败指针寻找匹配
            while current and char not in current.children:
                current = current.fail
            
            if not current:
                current = self.root
                continue
            
            current = current.children[char]
            
            # 记录匹配的模式串
            for pattern in current.patterns:
                if pattern not in results:
                    results[pattern] = []
                results[pattern].append(i - len(pattern) + 1)
        
        return results

# 测试代码
def test_multi_pattern_matching():
    # 生成测试数据，生成四个字符ABCD的随机串，长度 1000000
    import random
    text = ''.join(random.choice('ABCD') for _ in range(10000000))

    patterns = ["ABABD", "ABABC", "ABAB", "ABC", "ABD", "AB", "A"]
    
    print(f"文本长度: {len(text)}")
    print(f"模式串数量: {len(patterns)}")
    print(f"模式串: {patterns}")
    
    # 测试 KMP 多模式匹配
    start_time = time.time()
    kmp_results = kmp_multi_pattern(text, patterns)
    kmp_time = time.time() - start_time
    print(f"\nKMP 多模式匹配时间: {kmp_time:.6f} 秒")
    
    # 测试 Aho-Corasick 算法
    start_time = time.time()
    ac = AhoCorasick(patterns)
    ac_results = ac.search(text)
    ac_time = time.time() - start_time
    print(f"Aho-Corasick 匹配时间: {ac_time:.6f} 秒")
    
    # 验证结果是否一致
    print(f"\n结果一致性验证:")
    for pattern in patterns:
        kmp_matches = kmp_results.get(pattern, [])
        ac_matches = ac_results.get(pattern, [])
        print(f"模式串 '{pattern}': KMP 找到 {len(kmp_matches)} 个匹配, AC 找到 {len(ac_matches)} 个匹配")
        print(f"  KMP: {kmp_matches[:5]}..." if len(kmp_matches) > 5 else f"  KMP: {kmp_matches}")
        print(f"  AC:  {ac_matches[:5]}..." if len(ac_matches) > 5 else f"  AC:  {ac_matches}")
        print(f"  结果一致: {kmp_matches == ac_matches}")
    
    # 计算性能提升
    speedup = kmp_time / ac_time if ac_time > 0 else float('inf')
    print(f"\n性能对比: Aho-Corasick 比 KMP 快 {speedup:.2f} 倍")

if __name__ == "__main__":
    test_multi_pattern_matching()