# Python 顺序栈实现
class Stack:
    def __init__(self):
        self.data = []
    def push(self, x):
        """入栈操作"""
        self.data.append(x)
    def pop(self):
        """出栈操作"""
        if not self.data:
            raise Exception("空栈")
        return self.data.pop()
    def peek(self):
        """获取栈顶元素"""
        if not self.data:
            raise Exception("空栈")
        return self.data[-1]
    def is_empty(self):
        """检查栈是否为空"""
        return len(self.data)==0

# 栈使用示例
s = Stack()

s.push(1)
s.push(2)
s.push(3)
print(s.peek())  # 3
print(s.pop())  # 3
print(s.is_empty())  # False
print(s.peek())  # 2
print(s.pop())  # 2
print(s.is_empty())  # False
print(s.peek())  # 1
print(s.pop())  # 1
print(s.is_empty())  # True
#print(s.peek())  # 异常：空栈
#print(s.pop())  # 异常：空栈
