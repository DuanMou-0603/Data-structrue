def fibonacci(n):
    """递归计算斐波那契数列"""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



def dfs(graph, node, visited):
    """深度优先遍历"""
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# 定义图
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# 调用深度优先遍历
visited = set()
dfs(graph, 'A', visited)  # 输出: A B D E F C

def hanoi(n, source, auxiliary, target):
    """汉诺塔问题"""
    if n > 0:
        hanoi(n - 1, source, target, auxiliary)
        print(f"Move disk {n} from {source} to {target}")
        hanoi(n - 1, auxiliary, source, target)

hanoi(3, 'A', 'B', 'C')

def quicksort(arr):
    """快速排序"""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5]))
