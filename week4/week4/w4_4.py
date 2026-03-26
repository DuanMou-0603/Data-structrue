# 循环队列实现
class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.data = [None] * max_size
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, item):
        """入队"""
        if self.is_full():
            print("队列已满，无法入队")
            return
        self.data[self.rear] = item
        self.rear = (self.rear + 1) % self.max_size
        self.size += 1

    def dequeue(self):
        """出队"""
        if self.is_empty():
            print("队列为空，无法出队")
            return None
        item = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return item

    def is_empty(self):
        """判断队列是否为空"""
        return self.size == 0

    def is_full(self):
        """判断队列是否已满"""
        return self.size == self.max_size

    def display(self):
        """显示队列内容"""
        print(f"队列内容: {self.data}")
        print(f"front: {self.front}, rear: {self.rear}")


# 非循环队列（用于对比演示假溢出）
class NonCircularQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.data = [None] * max_size
        self.front = 0
        self.rear = 0
    
    def enqueue(self, item):
        """入队"""
        if self.rear == self.max_size:
            print("队列已满，无法入队（假溢出）")
            return
        self.data[self.rear] = item
        self.rear += 1
    
    def dequeue(self):
        """出队"""
        if self.front == self.rear:
            print("队列为空，无法出队")
            return None
        item = self.data[self.front]
        self.data[self.front] = None
        self.front += 1
        return item
    
    def is_empty(self):
        """判断队列是否为空"""
        return self.front == self.rear
    
    def is_full(self):
        """判断队列是否已满"""
        return self.rear == self.max_size
    
    def display(self):
        """显示队列内容"""
        print(f"队列内容: {self.data}")
        print(f"front: {self.front}, rear: {self.rear}")

# 测试队列
if __name__ == "__main__":
    print("=== 演示假溢出问题 ===")
    print("\n1. 非循环队列测试:")
    non_circular_queue = NonCircularQueue(5)
    non_circular_queue.enqueue(1)
    non_circular_queue.enqueue(2)
    non_circular_queue.enqueue(3)
    print("出队:", non_circular_queue.dequeue())  # 1
    print("出队:", non_circular_queue.dequeue())  # 2
    non_circular_queue.display()
    
    # 尝试入队新元素，会出现假溢出
    print("\n尝试入队4:")
    non_circular_queue.enqueue(4)
    non_circular_queue.display()
    print("尝试入队5:")
    non_circular_queue.enqueue(5)
    non_circular_queue.display()
    print("尝试入队6 (假溢出):")
    non_circular_queue.enqueue(6)  # 假溢出，虽然队列前面有空位
    non_circular_queue.display()
    
    print("\n2. 循环队列测试:")
    queue = Queue(5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("出队:", queue.dequeue())  # 1
    print("出队:", queue.dequeue())  # 2
    queue.display()

    # 循环队列可以利用前面的空位
    print("\n尝试入队4:")
    queue.enqueue(4)
    queue.display()
    print("尝试入队5:")
    queue.enqueue(5)
    queue.display()
    print("尝试入队6:")
    queue.enqueue(6)
    queue.display()
    print("尝试入队7:")
    queue.enqueue(7)
    queue.display()
    print(f"队列是否已满: {queue.is_full()}")
    
    # 尝试入队8，此时队列已满
    print("\n尝试入队8 (真溢出):")
    queue.enqueue(8)  # 真溢出，队列确实满了
    print(f"队列是否已满: {queue.is_full()}")
    
    print("\n3. 循环队列出队测试:")
    print("出队:", queue.dequeue())  # 3
    print("出队:", queue.dequeue())  # 4
    queue.display()
    
    # 再次入队
    print("\n尝试入队8:")
    queue.enqueue(8)
    queue.display()
    print(f"队列是否已满: {queue.is_full()}")
    
    # 显示队列状态
    print("\n最终队列状态:")
    queue.display()
