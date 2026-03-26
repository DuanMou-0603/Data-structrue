# 链队列实现
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None  # 队首指针
        self.rear = None   # 队尾指针
        self.size = 0      # 队列大小
    
    def enqueue(self, item):
        """入队操作"""
        new_node = Node(item)
        if self.is_empty():
            # 队列为空时，front和rear都指向新节点
            self.front = new_node
            self.rear = new_node
        else:
            # 队列不为空时，在队尾添加新节点
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
    
    def dequeue(self):
        """出队操作"""
        if self.is_empty():
            print("队列为空，无法出队")
            return None
        # 保存队首元素
        item = self.front.value
        # 移动front指针到下一个节点
        self.front = self.front.next
        # 如果队列为空，rear也置为None
        if self.front is None:
            self.rear = None
        self.size -= 1
        return item
    
    def is_empty(self):
        """判断队列是否为空"""
        return self.size == 0
    
    def get_size(self):
        """获取队列大小"""
        return self.size
    
    def display(self):
        """显示队列内容"""
        if self.is_empty():
            print("队列为空")
            return
        current = self.front
        print("队列内容: ", end="")
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

# 测试链队列
if __name__ == "__main__":
    queue = Queue()
    
    # 测试入队
    print("=== 测试入队操作 ===")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.display()
    print(f"队列大小: {queue.get_size()}")
    
    # 测试出队
    print("\n=== 测试出队操作 ===")
    print("出队元素:", queue.dequeue())
    queue.display()
    print(f"队列大小: {queue.get_size()}")
    
    # 测试连续出队
    print("\n=== 测试连续出队 ===")
    print("出队元素:", queue.dequeue())
    print("出队元素:", queue.dequeue())
    queue.display()
    print(f"队列大小: {queue.get_size()}")
    print(f"队列是否为空: {queue.is_empty()}")
    
    # 测试空队列出队
    print("\n=== 测试空队列出队 ===")
    queue.dequeue()
    
    # 测试空队列入队
    print("\n=== 测试空队列入队 ===")
    queue.enqueue(4)
    queue.enqueue(5)
    queue.display()
    print(f"队列大小: {queue.get_size()}")
    print(f"队列是否为空: {queue.is_empty()}")