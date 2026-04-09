import re

# ===================== 1. 基础字符串操作 vs 正则基础匹配 =====================
print("=" * 60)
print("1. 基础字符串查找 / 替换 / 分割 vs 正则")
print("=" * 60)
s = "Hello Python! Python 是最棒的编程语言 12345"

# 1.1 查找子串是否存在
print("\n【查找子串】")
# 字符串方法：简单直接，只能精确匹配
print("字符串方法：'Python' 在字符串中?", "Python" in s)
# 正则方法：match/search 匹配（search 全局查找，match 只匹配开头）
print("正则 search：匹配到 Python?", bool(re.search(r"Python", s)))

# 1.2 统计子串出现次数
print("\n【统计次数】")
print("字符串方法：Python 出现次数:", s.count("Python"))
# 正则：findall 统计匹配结果长度
print("正则 findall：Python 出现次数:", len(re.findall(r"Python", s)))

# 1.3 替换子串
print("\n【替换子串】")
print("字符串方法：替换 Python → Java:", s.replace("Python", "Java"))
# 正则替换：功能更强（支持模糊替换）
print("正则替换：替换 Python → Java:", re.sub(r"Python", "Java", s))

# 1.4 分割字符串
print("\n【分割字符串】")
test_str = "a,b c;d|e"
print("字符串方法：按空格分割:", test_str.split(" "))
# 正则：按 任意非字母 分割（强大的模糊分割）
print("正则分割：按非字母分割:", re.split(r"[^a-zA-Z]", test_str))

# ===================== 2. 字符串大小写/格式处理 =====================
print("\n" + "=" * 60)
print("2. 字符串大小写、去空格、格式化")
print("=" * 60)
s2 = "  hello WORLD 123  "

# 大小写转换
print("转大写:", s2.upper())
print("转小写:", s2.lower())
print("首字母大写:", s2.title())

# 去除首尾空白
print("去除首尾空格:", s2.strip())
print("去除左侧空格:", s2.lstrip())
print("去除右侧空格:", s2.rstrip())

# 字符串拼接/格式化
name = "小明"
age = 20
print("f-string 格式化:", f"姓名：{name}，年龄：{age}")

# ===================== 3. 字符串判断功能 (isxxx) =====================
print("\n" + "=" * 60)
print("3. 字符串类型判断 isxxx 方法")
print("=" * 60)
num_str = "12345"
letter_str = "abcDEF"
chinese_str = "你好"

print(f"'{num_str}' 是纯数字?", num_str.isdigit())
print(f"'{letter_str}' 是纯字母?", letter_str.isalpha())
print(f"'{num_str+letter_str}' 是字母+数字?", (num_str+letter_str).isalnum())
print(f"'{chinese_str}' 是中文?", chinese_str.isalpha())  # 中文也会判定为字母

# ===================== 4. 正则【高级功能】(字符串做不到) =====================
print("\n" + "=" * 60)
print("4. 正则高级功能 (字符串无法实现)")
print("=" * 60)
s3 = "我的电话：13812345678，邮箱：test@123.com，邮编：100000"

# 4.1 匹配手机号（模糊规则匹配）
print("\n【匹配手机号】")
phone_pattern = r"1[3-9]\d{9}"  # 正则规则：1开头+3-9+9位数字
print("正则匹配结果:", re.findall(phone_pattern, s3))

# 4.2 匹配邮箱
print("\n【匹配邮箱】")
email_pattern = r"\w+@\w+\.\w+"
print("正则匹配结果:", re.findall(email_pattern, s3))

# 4.3 提取所有数字
print("\n【提取所有数字】")
print("正则提取所有数字:", re.findall(r"\d+", s3))

# 4.4 替换所有数字为 *
print("\n【模糊替换：数字脱敏】")
print("正则脱敏数字:", re.sub(r"\d", "*", s3))

# 4.5 开头/结尾匹配
print("\n【开头/结尾匹配】")
print("正则匹配以 我的 开头?", bool(re.match(r"^我的", s3)))
print("正则匹配以 00 结尾?", bool(re.search(r"00$", s3)))

# ===================== 5. 正则分组提取 =====================
print("\n" + "=" * 60)
print("5. 正则分组提取关键信息")
print("=" * 60)
info = "姓名：张三，年龄：25，城市：北京"
# 分组：用()包裹要提取的内容
pattern = r"姓名：(.*?)，年龄：(\d+)，城市：(.*?)"
result = re.search(pattern, info)
if result:
    print("分组提取结果：")
    print("姓名:", result.group(1))
    print("年龄:", result.group(2))
    print("城市:", result.group(3))
