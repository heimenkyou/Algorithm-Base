import os
import sys
import re


def create_lg_problem():
    print("新建题目模板 - Luogu（洛谷）")
    # 1. 直接获取手动输入
    raw_input = input("请输入洛谷题目全名 (如 P1023 ...): ").strip()

    if not raw_input:
        print("错误：输入不能为空")
        return

    # 2. 自动提取题号并拼接链接 (匹配开头的 P1024, CF123A 等格式)
    match = re.match(r"^([A-Z0-9]+)", raw_input, re.I)
    if not match:
        print("错误：无法识别题号")
        return

    problem_id = match.group(1).upper()
    title = raw_input
    link = f"https://www.luogu.com.cn/problem/{problem_id}"

    # 3. 定位 Luogu 目录
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    base_dir = os.path.join(project_root, "Luogu")
    problem_path = os.path.join(base_dir, title)

    if os.path.exists(problem_path):
        print(f"文件夹已存在: {problem_path}")
    else:
        os.makedirs(problem_path, exist_ok=True)
        print(f"已创建文件夹: {title}")

    # 4. 生成模板文件
    py_file = os.path.join(problem_path, "solution.py")
    if not os.path.exists(py_file):
        with open(py_file, "w", encoding="utf-8") as f:
            f.write(f"# {link}\n\n")
            f.write("import sys\n\n")
            f.write("def main():\n")
            f.write("    pass\n\n")
            f.write("if __name__ == '__main__':\n")
            f.write("    main()\n")

    md_file = os.path.join(problem_path, "README.md")
    if not os.path.exists(md_file):
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write(f"[题目链接]({link})\n\n---\n\n## 解题思路\n")

    print("模板文件初始化完成。")


if __name__ == "__main__":
    # 确保 Windows 下输出不乱码
    if sys.stdout.encoding != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")
    create_lg_problem()
