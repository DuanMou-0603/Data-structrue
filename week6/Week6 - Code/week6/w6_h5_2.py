# 先安装库：pip install pyahocorasick
import ahocorasick

def ac_automaton_multi_match(target_str: str, keywords: list[str]) -> dict:
    """
    海量多模式匹配（工程最佳实践：成熟AC自动机库，避免手写）
    """
    # 安全边界
    if not isinstance(target_str, str):
        raise TypeError("目标字符串必须是字符串")
    if not isinstance(keywords, list) or len(keywords) == 0:
        raise ValueError("关键词列表不能为空且必须是列表类型")

    # 构建AC自动机（生产环境可全局单例，避免重复构建）
    ac = ahocorasick.Automaton()
    for idx, keyword in enumerate(keywords):
        ac.add_word(keyword, (idx, keyword))
    ac.make_automaton()  # 构建失败会抛异常，外层可捕获

    # 执行匹配
    matched_keywords = set()
    for end_index, (insert_order, keyword) in ac.iter(target_str):
        matched_keywords.add(keyword)

    return {
        "matched_keywords": list(matched_keywords),
        "match_count": len(matched_keywords),
        "status": "success"
    }

# 测试
if __name__ == "__main__":
    # 海量关键词示例（可扩展到10万+）
    keyword_list = ["Python", "工程实践", "AC自动机", "异常处理"]
    test_text = "Python工程最佳实践，使用AC自动机处理海量关键词匹配"
    print(ac_automaton_multi_match(test_text, keyword_list))