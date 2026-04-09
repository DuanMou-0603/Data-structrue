def simple_string_match(target_str: str, keyword: str) -> dict:
    """
    简单字符串匹配（工程最佳实践：优先内置方法）
    :param target_str: 目标字符串
    :param keyword: 查找关键词
    :return: 查找结果（存在性、索引、安全边界）
    """
    # 1. 安全边界校验（生产必备：空值、空字符串防护）
    if not isinstance(target_str, str) or not isinstance(keyword, str):
        raise TypeError("目标字符串和关键词必须是字符串类型")
    if not keyword:
        raise ValueError("查找关键词不能为空")

    # 2. 优先使用内置 in / str.find()（底层优化极快）
    is_exist = keyword in target_str
    find_index = target_str.find(keyword)  # 找不到返回 -1，无异常

    # 3. 标准化返回（生产代码可读性、可维护性）
    return {
        "keyword_exists": is_exist,
        "first_occurrence_index": find_index,
        "status": "success"
    }


import re

def complex_pattern_match(target_str: str) -> dict:
    """
    复杂规则匹配（工程最佳实践：标准库 re）
    场景：提取字符串中的手机号、邮箱
    """
    # 安全边界
    if not isinstance(target_str, str):
        raise TypeError("输入必须是字符串")

    # 预编译正则（生产必备：多次调用提升性能）
    phone_pattern = re.compile(r"1[3-9]\d{9}")  # 手机号规则
    email_pattern = re.compile(r"\w+@\w+\.\w+")  # 邮箱规则

    # 异常防护：正则执行异常捕获
    try:
        phones = phone_pattern.findall(target_str)
        emails = email_pattern.findall(target_str)
    except re.error as e:
        return {"error": f"正则匹配失败：{str(e)}", "status": "failed"}

    return {
        "phones": phones,
        "emails": emails,
        "match_count": len(phones) + len(emails),
        "status": "success"
    }

# 测试
if __name__ == "__main__":
    test_text = "Python工程最佳实践：优先使用内置方法"
    print(simple_string_match(test_text, "工程"))  # 存在
    print(simple_string_match(test_text, "Java"))  # 不存在
    test_text = "联系我：13800138000，邮箱：test@example.com"
    print(complex_pattern_match(test_text))