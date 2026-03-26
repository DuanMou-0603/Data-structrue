# 递归版本 (Recursion)
def reverse_rec(head):
    """递归方式反转链表"""
    # 基线条件：如果链表为空或只有一个节点，直接返回头节点
    # 因为单个节点的链表反转后还是自己
    if not head or not head.next:
        return head
    
    # 递归调用：先反转当前节点之后的所有节点
    # new_head 最终会指向原链表的尾节点（反转后的头节点）
    new_head = reverse_rec(head.next)
    
    # 将当前节点的下一个节点的next指针指向当前节点
    # 实现链表的局部反转
    head.next.next = head
    
    # 将当前节点的next指针置为None，避免形成环
    # 当递归回溯到原链表头节点时，它会成为新链表的尾节点
    head.next = None
    
    # 返回新的头节点（原链表的尾节点）
    return new_head

# 迭代版本 (Iteration)
def reverse_iter(head):
    """迭代方式反转链表"""
    # 初始化前一个节点为None（反转后链表的尾节点）
    prev = None
    # 初始化当前节点为原链表的头节点
    cur = head
    # 遍历链表，直到当前节点为None
    while cur:
        # 保存当前节点的下一个节点，避免反转后丢失
        next_node = cur.next
        # 将当前节点的next指针指向前一个节点，实现反转
        cur.next = prev
        # 将前一个节点更新为当前节点，为下一次反转做准备
        prev = cur
        # 将当前节点更新为下一个节点，继续遍历
        cur = next_node
    # 当遍历结束时，prev指向原链表的尾节点，即反转后链表的头节点
    return prev

# 定义链表节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 创建测试链表: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# 测试递归版本
print("递归版本测试:")
new_head_rec = reverse_rec(head)
current = new_head_rec
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

# 重新创建测试链表
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# 测试迭代版本
print("迭代版本测试:")
new_head_iter = reverse_iter(head)
current = new_head_iter
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")