# 栈使用示例 - 括号匹配验证
from w4_1 import Stack

def is_valid_parentheses(s):
    """验证括号匹配"""
    stack = Stack()
    # 括号匹配字典
    pairs = {")": "(", "]": "[", "}": "{"}
    
    print("初始状态：栈为空，准备开始遍历表达式 `{}`。".format(s))
    
    for i, char in enumerate(s):
        if char in "([{":
            # 左括号入栈
            stack.push(char)
            print("步骤{}：读取左括号 `{}` 入栈，栈内元素：{}".format(i+1, char, stack.data))
        elif char in ")]}":
            # 右括号匹配
            if stack.is_empty():
                print("步骤{}：读取右括号 `{}`，栈为空，匹配失败".format(i+1, char))
                return False
            top_char = stack.pop()
            if top_char != pairs[char]:
                print("步骤{}：读取右括号 `{}`，与栈顶 `{}` 不匹配，验证失败".format(i+1, char, top_char))
                return False
            print("步骤{}：读取右括号 `{}`，匹配栈顶 `{}` 后出栈，栈内：{}".format(i+1, char, top_char, stack.data))
    
    if stack.is_empty():
        print("最终状态：表达式遍历完毕且栈为空，括号匹配验证通过")
        return True
    else:
        print("最终状态：表达式遍历完毕但栈不为空，括号匹配验证失败")
        return False

# 测试示例
if __name__ == "__main__":
    # 测试用例1：匹配成功
    print("\n测试用例1: ([{}])")
    result = is_valid_parentheses("([{}])")
    print("验证结果：", result)
    
    # 测试用例2：匹配失败 - 右括号多余
    print("\n测试用例2: ([{}])]")
    result = is_valid_parentheses("([{}])]")
    print("验证结果：", result)
    
    # 测试用例3：匹配失败 - 左括号多余
    print("\n测试用例3: ([{})")
    result = is_valid_parentheses("([{})")
    print("验证结果：", result)