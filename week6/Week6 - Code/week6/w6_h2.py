class TrieNode:
    def __init__(self):
        self.children = {}  # 子节点
        self.is_end = False  # 是否是模式结尾
        self.fail = None  # 失败指针（AC自动机用）


# 构建 Trie
def build_trie(patterns):
    root = TrieNode()
    for pat in patterns:
        node = root
        for c in pat:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True
    return root


# 构建 AC 自动机的失败指针
def build_fail(root):
    from collections import deque
    queue = deque()

    # 根节点的所有子节点的失败指针指向根节点
    for char, child in root.children.items():
        child.fail = root
        queue.append(child)

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
                child.fail = root

            # 合并模式串标记
            child.is_end = child.is_end or child.fail.is_end
            queue.append(child)


# 打印函数
def print_trie(root, prefix="", is_last=True):
    """清晰打印 Trie 树 + AC 自动机失败指针"""
    # 递归终止
    if not root:
        return

    children = list(root.children.items())
    # 遍历子节点（核心打印逻辑）
    for i, (char, child) in enumerate(children):
        # 判断是否最后一个子节点
        last = (i == len(children) - 1)

        # 拼接显示：字符 + 结束标记
        end_mark = " (End)" if child.is_end else ""
        connector = "└── " if last else "├── "
        print(f"{prefix}{connector}{char}{end_mark}")

        # 打印失败指针
        if child.fail is not None:
            fail_target = "Root" if child.fail == root else "Node"
            print(f"{prefix}{'    ' if last else '│   '}(Fail → {fail_target})")

        # 递归打印子节点
        new_prefix = prefix + ("    " if last else "│   ")
        print_trie(child, new_prefix, last)


# 测试
if __name__ == "__main__":
    patterns = ["Joe", "John", "Johnny", "Jane", "Jack"]
    # 构建 Trie 树
    root = build_trie(patterns)
    print("========== Trie 树结构 ==========\nRoot")
    print_trie(root)

    # 构建 AC 自动机失败指针
    build_fail(root)
    print("\n========== AC 自动机结构 ==========\nRoot")
    print_trie(root)