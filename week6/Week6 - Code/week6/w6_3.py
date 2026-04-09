# 串存储模式

# 顺序存储示例
print("=== 顺序存储示例 ===")
s = 'abcdefgh'
print("原始字符串:", s)
print("访问第一个字符:", s[0])
print("截取子串[1:5]:", s[1:5])
print("字符串拼接:", s[1:5] + 'fgh')


# 链式存储实现
class Node:
    def __init__(self, char):
        self.char = char
        self.next = None


class LinkedListString:
    def __init__(self, s):
        self.head = None
        if s:
            self.head = Node(s[0])
            current = self.head
            for char in s[1:]:
                current.next = Node(char)
                current = current.next

    def __str__(self):
        """将链式存储转换为字符串以便打印"""
        result = []
        current = self.head
        while current:
            result.append(current.char)
            current = current.next
        return ''.join(result)

    def get_char(self, index):
        """获取指定位置的字符"""
        if index < 0:
            return None
        current = self.head
        for i in range(index):
            if not current:
                return None
            current = current.next
        return current.char if current else None

    def substring(self, start, end):
        """截取子串"""
        result = []
        current = self.head
        # 移动到起始位置
        for i in range(start):
            if not current:
                return ''
            current = current.next
        # 收集子串字符
        for i in range(start, end):
            if not current:
                break
            result.append(current.char)
            current = current.next
        return ''.join(result)

    def concatenate(self, other):
        """字符串拼接"""
        # 先转换为字符串再拼接，实际链式存储的拼接会更复杂
        return str(self) + other


# 链式存储示例
print("\n=== 链式存储示例 ===")
linked_s = LinkedListString('abcdefgh')
print("原始字符串:", linked_s)
print("访问第一个字符:", linked_s.get_char(0))
print("截取子串[1:5]:", linked_s.substring(1, 5))
print("字符串拼接:", linked_s.concatenate('fgh'))

# 对比两种存储方式的特点
print("\n=== 存储方式对比 ===")
print("顺序存储:")
print("- 优点: 随机访问快，时间复杂度O(1)")
print("- 缺点: 插入删除操作需要移动元素，时间复杂度O(n)")
print("链式存储:")
print("- 优点: 插入删除操作方便，时间复杂度O(1)")
print("- 缺点: 随机访问慢，时间复杂度O(n)")