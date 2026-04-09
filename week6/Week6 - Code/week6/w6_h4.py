import time
import random

# AC 自动机节点
class TrieNode:
    def __init__(self):
        self.children = {}     # 子节点
        self.is_end = False    # 是否是模式结尾
        self.fail = None      # 失败指针
        self.patterns = []     # 存储以当前节点结尾的模式串

# 构建 Trie
def build_trie_with_patterns(patterns):
    root = TrieNode()
    for pat in patterns:
        node = root
        for c in pat:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True
        node.patterns.append(pat)
    return root

# 构建失败指针
def build_fail_with_patterns(root):
    from collections import deque
    queue = deque()

    # 根节点子节点 fail 指向 root
    for char, child in root.children.items():
        child.fail = root
        queue.append(child)

    while queue:
        current = queue.popleft()

        for char, child in current.children.items():
            fail_node = current.fail
            while fail_node and char not in fail_node.children:
                fail_node = fail_node.fail

            # 设置失败指针
            if fail_node:
                child.fail = fail_node.children[char]
            else:
                child.fail = root

            child.patterns += child.fail.patterns

            child.is_end = child.is_end or child.fail.is_end
            queue.append(child)

# AC 自动机搜索
def ac_search(text, root):
    results = {}
    current = root

    for i, char in enumerate(text):
        # 沿着失败指针回退
        while current and char not in current.children:
            current = current.fail
        if not current:
            current = root
            continue

        current = current.children[char]

        # 取出所有匹配的模式串
        for pattern in current.patterns:
            if pattern not in results:
                results[pattern] = []
            # 计算起始位置
            pos = i - len(pattern) + 1
            results[pattern].append(pos)

    return results

# ==================== KMP 相关 ====================
def kmp_match(s, p):
    """KMP 单模式匹配"""
    def build_next(p):
        m = len(p)
        next_arr = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and p[i] != p[j]:
                j = next_arr[j-1]
            if p[i] == p[j]:
                j += 1
            next_arr[i] = j
        return next_arr

    n, m = len(s), len(p)
    if m == 0:
        return []
    next_arr = build_next(p)
    j = 0
    matches = []
    for i in range(n):
        while j > 0 and s[i] != p[j]:
            j = next_arr[j-1]
        if s[i] == p[j]:
            j += 1
        if j == m:
            matches.append(i - m + 1)
            j = next_arr[j-1]
    return matches

def kmp_multi_pattern(text, patterns):
    results = {}
    for pattern in patterns:
        results[pattern] = kmp_match(text, pattern)
    return results

# ==================== 测试 ====================
def test_multi_pattern_search():
    # 生成测试文本
    text = ''.join(random.choice('Johneyakc') for _ in range(1000000))
    patterns = ["Joe", "John", "Johnny", "Jane", "Jack"]

    print(f"文本长度: {len(text)}")
    print(f"模式串: {patterns}")

    # KMP
    start = time.time()
    kmp_res = kmp_multi_pattern(text, patterns)
    kmp_time = time.time() - start
    print(f"\nKMP 耗时: {kmp_time:.4f}s")

    # AC 自动机
    start = time.time()
    root = build_trie_with_patterns(patterns)
    build_fail_with_patterns(root)
    ac_res = ac_search(text, root)
    ac_time = time.time() - start
    print(f"AC  耗时: {ac_time:.4f}s")

    # 结果对比
    print("\n=== 结果一致性验证 ===")
    for pat in patterns:
        kmp_cnt = len(kmp_res[pat])
        ac_cnt = len(ac_res.get(pat, []))
        ok = kmp_res[pat] == ac_res.get(pat, [])
        print(f"{pat:8} | KMP:{kmp_cnt:4} | AC:{ac_cnt:4} | 一致:{ok}")

    # 性能倍数
    print(f"\nAC 比 KMP 快 {kmp_time/ac_time:.2f} 倍")

if __name__ == "__main__":
    test_multi_pattern_search()