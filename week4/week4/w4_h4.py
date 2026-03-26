# 二叉树前序遍历递归实现
def preorderTraversal_rec(root):
    """递归实现二叉树前序遍历"""
    res = []
    # 内置 helper 函数，用于递归遍历
    def helper(node):
        if not node:
            return
        res.append(node.val)
        helper(node.left)
        helper(node.right)
    helper(root)
    return res

# 二叉树前序遍历迭代实现
def preorderTraversal(root):
    """迭代实现二叉树前序遍历
    
    核心思想：使用栈模拟递归过程
    前序遍历顺序：根节点 → 左子树 → 右子树
    
    关键规则：右先入栈，左后入栈
    """
    if not root:
        return []
    
    # 初始化栈，将根节点入栈
    stack, res = [root], []
    print("初始化栈:", [node.val for node in stack])
    
    while stack:
        # 1. 弹出栈顶节点并访问
        node = stack.pop()
        res.append(node.val)
        print(f"弹出节点 {node.val}，当前结果: {res}")
        
        # 2. 右子节点先入栈
        if node.right:
            stack.append(node.right)
            print(f"右子节点 {node.right.val} 入栈，栈状态: {[n.val for n in stack]}")
        
        # 3. 左子节点后入栈
        if node.left:
            stack.append(node.left)
            print(f"左子节点 {node.left.val} 入栈，栈状态: {[n.val for n in stack]}")
    
    return res


# 定义二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 创建测试二叉树
#       1
#      / \
#     2   3
#    / \
#   4   5
#  / \
# 6   7
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(6)
root.left.left.right = TreeNode(7)


# 测试递归实现
print("递归实现前序遍历:")
print(preorderTraversal_rec(root))  # 输出: [1, 2, 4, 6, 7, 5, 3]

# 测试迭代实现
print("迭代实现前序遍历:")
print(preorderTraversal(root))      # 输出: [1, 2, 4, 6, 7, 5, 3]