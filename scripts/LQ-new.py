import os
import sys

def create_lq_problem():
    # 1. 直接获取手动输入
    title = input("请输入题目名称: ").strip()
    raw_link = input("请输入题目链接: ").strip()
    
    if not title or not raw_link:
        print("错误：名称或链接不能为空")
        return

    # 2. 自动处理链接，去掉 ? 之后的部分
    link = raw_link.split('?')[0]

    # 3. 定位 Lanqiao 目录
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    base_dir = os.path.join(project_root, "Lanqiao")
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
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
    create_lq_problem()