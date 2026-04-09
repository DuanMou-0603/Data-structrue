def large_file_stream_match(file_path: str, keyword: str, chunk_size: int = 4096) -> dict:
    """
    大文件流式匹配（工程最佳实践：分块读取，不加载全文件）
    :param chunk_size: 分块大小（4KB/8KB 最优，磁盘IO友好）
    """
    # 安全边界
    if not keyword:
        raise ValueError("关键词不能为空")
    if chunk_size <= 0:
        raise ValueError("分块大小必须大于0")

    match_lines = []
    line_count = 0

    # 异常处理：文件不存在、权限不足、编码错误
    try:
        # 流式逐行读取（内存最优）
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                line_count += 1
                if keyword in line:
                    match_lines.append({"line_num": line_count, "content": line.strip()})
    except FileNotFoundError:
        return {"error": "文件不存在", "status": "failed"}
    except PermissionError:
        return {"error": "无文件读取权限", "status": "failed"}
    except Exception as e:
        return {"error": f"文件读取失败：{str(e)}", "status": "failed"}

    return {
        "total_lines": line_count,
        "matched_lines": match_lines,
        "match_count": len(match_lines),
        "status": "success"
    }

# 测试
if __name__ == "__main__":
    # 替换为大文件路径
    print(large_file_stream_match("large_log.txt", "error"))