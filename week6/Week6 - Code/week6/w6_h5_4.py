from typing import Literal

from week6.w6_h5_1 import simple_string_match, complex_pattern_match
from week6.w6_h5_2 import ac_automaton_multi_match
from week6.w6_h5_3 import large_file_stream_match


def universal_matcher(
        data: str,
        pattern: str | list[str],
        match_type: Literal["simple", "regex", "ac", "large_file"] = "simple",
        file_path: str = None
) -> dict:
    """
    通用匹配引擎（生产级封装：自动选择最优算法）
    遵循：内置优先 → 标准库 → 成熟库 → 流式处理
    """
    try:
        # 统一安全边界校验
        if match_type != "large_file" and not isinstance(data, str):
            return {"error": "非文件模式必须输入字符串", "status": "failed"}

        # 策略路由：不同机制自动切换
        if match_type == "simple":
            return simple_string_match(data, pattern)
        elif match_type == "regex":
            return complex_pattern_match(data)
        elif match_type == "ac":
            return ac_automaton_multi_match(data, pattern)
        elif match_type == "large_file":
            return large_file_stream_match(file_path, pattern)
        else:
            return {"error": "不支持的匹配类型", "status": "failed"}

    except Exception as e:
        # 全局异常（生产必备：不崩溃、返回标准化错误）
        return {
            "error": f"匹配执行失败：{str(e)}",
            "status": "failed",
            "error_type": type(e).__name__
        }


# 机制切换
if __name__ == "__main__":
    test_data = "Python工程实践 13800138000 test@example.com"

    # 1. 简单匹配
    print(universal_matcher(test_data, "工程"))

    # 2. 正则匹配
    print(universal_matcher(test_data, "", "regex"))

    # 3. AC自动机多模式匹配
    print(universal_matcher(test_data, ["Python", "工程"], "ac"))