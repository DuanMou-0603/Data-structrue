import random
import string

# 线性时间复杂度
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list2 = list(range(1000))

str1 = "hello world"

# 长度为 n 的字符串
def generate_random_str(length):
    return ''.join(random.choice(string.ascii_lowercase+string.digits) for _ in range(length))

str2 = generate_random_str(1000)

print(list1, list2, str1, str2, sep='\n')

# 2 维矩阵
matrix = [[random.randint(0, 100) for _ in range(10)] for _ in range(10)]
print(matrix)

# n 维矩阵
def generate_random_matrix(shape):
    if len(shape) == 1:
        return [random.randint(0, 100) for _ in range(shape[0])]
    else:
        return [generate_random_matrix(shape[1:]) for _ in range(shape[0])]

print(generate_random_matrix([2, 3, 4, 5, 6]))


class TreeNode:
    """二叉树节点类"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left  # 左子节点
        self.right = right  # 右子节点

# 构建二叉树：
#       1
#      / \
#     2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# 前序遍历（根-左-右）
def pre_order(node):
    if node:
        print(node.val, end=" ")
        pre_order(node.left)
        pre_order(node.right)

pre_order(root)  # 输出：1 2 3


# 无向图（邻接表表示）
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}
# 遍历图（深度优先）
def dfs(node, visited):
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)
