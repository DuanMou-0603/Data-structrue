from abc import ABC, abstractmethod
from typing import Any, Iterator, List as PyList


# ===================== 抽象基类：定义通用接口规范 =====================
class AbstractCollection(ABC):
    """所有集合的抽象基类，定义通用方法"""
    @abstractmethod
    def is_empty(self) -> bool:
        """判断集合是否为空"""
        pass

    @abstractmethod
    def size(self) -> int:
        """获取集合元素个数"""
        pass

    @abstractmethod
    def clear(self) -> None:
        """清空集合所有元素"""
        pass


class AbstractList(AbstractCollection):
    """抽象列表：定义列表必须实现的核心接口"""
    @abstractmethod
    def add(self, item: Any) -> None:
        """尾部添加元素"""
        pass

    @abstractmethod
    def insert(self, index: int, item: Any) -> None:
        """指定索引插入元素"""
        pass

    @abstractmethod
    def remove(self, item: Any) -> None:
        """删除第一个匹配的元素"""
        pass

    @abstractmethod
    def get(self, index: int) -> Any:
        """根据索引获取元素"""
        pass

    @abstractmethod
    def __getitem__(self, index: int) -> Any:
        """支持 [] 索引访问"""
        pass


class AbstractStack(AbstractCollection):
    """抽象栈：定义栈必须实现的核心接口（LIFO）"""
    @abstractmethod
    def push(self, item: Any) -> None:
        """入栈：向栈顶添加元素"""
        pass

    @abstractmethod
    def pop(self) -> Any:
        """出栈：移除并返回栈顶元素"""
        pass

    @abstractmethod
    def peek(self) -> Any:
        """查看栈顶元素（不删除）"""
        pass


# ===================== 具体实现类：基于抽象接口 =====================
class MyList(AbstractList):
    """自定义动态列表：基于Python列表实现"""
    def __init__(self):
        self._items: PyList[Any] = []  # 私有存储容器

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

    def clear(self) -> None:
        self._items.clear()

    def add(self, item: Any) -> None:
        self._items.append(item)

    def insert(self, index: int, item: Any) -> None:
        self._items.insert(index, item)

    def remove(self, item: Any) -> None:
        if self.is_empty():
            raise ValueError("列表为空，无法删除元素")
        try:
            self._items.remove(item)
        except ValueError:
            raise ValueError(f"元素 {item} 不在列表中")

    def get(self, index: int) -> Any:
        if index < 0 or index >= self.size():
            raise IndexError("索引超出范围")
        return self._items[index]

    def __getitem__(self, index: int) -> Any:
        return self.get(index)

    def __str__(self) -> str:
        return str(self._items)

    def __iter__(self) -> Iterator[Any]:
        """支持迭代遍历"""
        return iter(self._items)


class MyStack(AbstractStack):
    """栈实现：基于Python列表，栈顶在列表尾部（高效操作）"""
    def __init__(self):
        self._items: PyList[Any] = []  # 私有存储容器

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

    def clear(self) -> None:
        self._items.clear()

    def push(self, item: Any) -> None:
        self._items.append(item)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("栈为空，无法执行出栈操作")
        return self._items.pop()

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("栈为空，无法查看栈顶元素")
        return self._items[-1]

    def __str__(self) -> str:
        return f"Stack({self._items})"


# ===================== 测试用例 =====================
if __name__ == "__main__":
    print("=== 测试自定义列表 ===")
    my_list = MyList()
    my_list.add(10)
    my_list.add(20)
    my_list.insert(0, 5)
    print("列表内容:", my_list)
    print("索引1元素:", my_list[1])
    my_list.remove(10)
    print("删除10后:", my_list)

    print("\n=== 测试栈 ===")
    stack = MyStack()
    stack.push("A")
    stack.push("B")
    stack.push("C")
    print("栈内容:", stack)
    print("栈顶元素:", stack.peek())
    print("出栈:", stack.pop())
    print("出栈后栈内容:", stack)
    print("栈大小:", stack.size())