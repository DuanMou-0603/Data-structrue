# 链栈实现
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, x):
        """入栈操作"""
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        """出栈操作"""
        if self.is_empty():
            raise Exception("空栈")
        value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return value

    def peek(self):
        """获取栈顶元素"""
        if self.is_empty():
            raise Exception("空栈")
        return self.top.value

    def is_empty(self):
        """检查栈是否为空"""
        return self.size == 0

# 栈使用示例
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())  # 3
print(s.pop())   # 3
print(s.is_empty())  # False
print(s.peek())  # 2
print(s.pop())   # 2
print(s.is_empty())  # False
print(s.peek())  # 1
print(s.pop())   # 1
print(s.is_empty())  # True
# print(s.peek())  # 异常：空栈
# print(s.pop())   # 异常：空栈

