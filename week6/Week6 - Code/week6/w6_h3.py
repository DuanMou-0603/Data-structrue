import time
import random


# AC 自动机节点
class TrieNode:
    def __init__(self):
        self.children = {}  # 子节点
        self.is_end = False  # 是否是模式结尾
        self.fail = None  # 失败指针
        self.patterns = []  # 存储以当前节点结尾的模式串


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


def ac_search_with_print(text, root):
    """带执行过程打印的 AC 自动机搜索"""
    results = {}
    current = root
    print("=" * 60)
    print("AC 自动机 匹配执行过程")
    print("=" * 60)

    for idx, char in enumerate(text):
        print(f"\n[{idx}] 正在处理字符：'{char}'")

        # 失败指针跳转
        while current and char not in current.children:
            print(f"   字符不存在，跳转到失败指针")
            current = current.fail

        if not current:
            print(f"   回退到根节点")
            current = root
            continue

        # 走到子节点
        prev = current
        current = current.children[char]
        print(f"   从节点移动 → '{char}'")

        # 检查匹配
        if current.patterns:
            print(f"   找到匹配：{current.patterns}，位置：", end="")
            for pat in current.patterns:
                pos = idx - len(pat) + 1
                print(f"{pat}@{pos}", end=" ")
                if pat not in results:
                    results[pat] = []
                results[pat].append(pos)
            print()

    print("\n" + "=" * 60)
    print("匹配结束，最终结果：", results)
    print("=" * 60)
    return results


# ===================== 测试 =====================
if __name__ == "__main__":
    # 演示匹配过程
    text = "Hello Joe! Johnny Joe & Jane"
    patterns = ["Joe", "John", "Johnny", "Jane", "Jack"]

    # 构建 AC 自动机
    root = build_trie_with_patterns(patterns)
    build_fail_with_patterns(root)

    print("待匹配文本：", text)
    print("模式串：", patterns)
    ac_search_with_print(text, root)