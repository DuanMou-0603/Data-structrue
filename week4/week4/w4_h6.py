def pause():
    """按回车继续"""
    input("")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head, desc="当前链表："):
    """打印链表"""
    nodes = []
    cur = head
    while cur:
        nodes.append(str(cur.val))
        cur = cur.next
    print(desc, " -> ".join(nodes) if nodes else "空")

# ======================
# 递归反转链表（带调试打印）
# ======================
def reverse_list_recursive(head, depth=0):
    indent = "|    " * depth  # 栈深度缩进

    # --------------------
    # 【第一步：进入递归】
    # --------------------
    print(f"{indent}进入递归层 depth={depth}, 当前 head = {head.val if head else 'None'}")
    print_linked_list(head, f"{indent}当前层链表：")

    pause()

    # 递归终止条件：走到最后一个节点
    if not head or not head.next:
        print(f"{indent}到达递归终点！返回 head = {head.val if head else 'None'}")
        pause()
        return head

    # 保存下一个节点（方便观察）
    next_node = head.next

    # --------------------
    # 【第二步：深入递归】
    # --------------------
    print(f"{indent}递归调用下一层：reverse({next_node.val})")
    new_head = reverse_list_recursive(head.next, depth + 1)

    # --------------------
    # 【第三步：回溯 → 反转指针】
    # --------------------
    print(f"{indent}开始回溯！当前层 head={head.val}, next={next_node.val}")
    print(f"{indent}执行：{next_node.val}.next = {head.val}")

    pause()

    # 核心反转操作
    head.next.next = head
    head.next = None  # 断开旧指针

    print(f"{indent}反转完成：{next_node.val} -> {head.val}，{head.val} -> None")
    print_linked_list(new_head, f"{indent}反转后局部链表：")

    pause()

    # 返回最终的头节点
    print(f"{indent}返回新链表头：{new_head.val}")
    return new_head


if __name__ == "__main__":
    # 构建链表 1 -> 2 -> 3 -> 4 -> 5
    print("===== 递归反转链表：调用栈 + 指针变化 演示 =====")
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("初始链表：")
    print_linked_list(head)

    pause()

    # 开始递归反转
    new_head = reverse_list_recursive(head)

    print("最终反转结果：")
    print_linked_list(new_head)