"""
使用方法：
1. 复制力扣网站题目描述中的标题
2. 运行脚本

这个脚本会直接从剪贴板读取标题和链接，
然后在 LeetCode 目录下创建对应题目的文件夹和模板文件。
"""

import ctypes
import os
import re
import sys


CF_UNICODETEXT = 13

user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

# 这些声明用于让 ctypes 正确调用 Windows 剪贴板 API。
user32.OpenClipboard.argtypes = [ctypes.c_void_p]
user32.OpenClipboard.restype = ctypes.c_bool
user32.CloseClipboard.argtypes = []
user32.CloseClipboard.restype = ctypes.c_bool
user32.GetClipboardData.argtypes = [ctypes.c_uint]
user32.GetClipboardData.restype = ctypes.c_void_p
user32.RegisterClipboardFormatW.argtypes = [ctypes.c_wchar_p]
user32.RegisterClipboardFormatW.restype = ctypes.c_uint
kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
kernel32.GlobalLock.restype = ctypes.c_void_p
kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
kernel32.GlobalUnlock.restype = ctypes.c_bool
kernel32.GlobalSize.argtypes = [ctypes.c_void_p]
kernel32.GlobalSize.restype = ctypes.c_size_t


def read_clipboard_bytes(format_id):
    # 按指定格式读取剪贴板的原始字节数据。
    user32.OpenClipboard(None)
    try:
        handle = user32.GetClipboardData(format_id)
        pointer = kernel32.GlobalLock(handle)
        try:
            return ctypes.string_at(pointer, kernel32.GlobalSize(handle))
        finally:
            kernel32.GlobalUnlock(handle)
    finally:
        user32.CloseClipboard()


def get_clipboard_text():
    # 纯文本格式里直接保存着题目标题。
    return read_clipboard_bytes(CF_UNICODETEXT).decode("utf-16-le").rstrip("\x00").strip()


def get_clipboard_html():
    # HTML 格式里包含了题目标题对应的 href。
    html_format = user32.RegisterClipboardFormatW("HTML Format")
    return read_clipboard_bytes(html_format).decode("utf-8").rstrip("\x00")


def get_problem_from_clipboard():
    # 组合纯文本标题和 HTML 里的 href，得到题目名称与链接。
    title = get_clipboard_text()
    html = get_clipboard_html()
    match = re.search(r'href="([^"]+)"', html)
    if not match:
        print("未识别到力扣题目链接，请先复制力扣题目描述中的标题。")
        print(f"当前剪贴板标题: {title or '<空>'}")
        preview = html[:200].replace("\n", "\\n")
        print(f"当前剪贴板 HTML 前 200 个字符: {preview or '<空>'}")
        raise ValueError("剪贴板中没有找到题目链接")

    link = match.group(1).strip()
    return title, link


def resolve_problem_path(base_dir, title):
    # 只有在目录已存在时，才要求输入一个新的题目名称。
    current_title = title

    while True:
        problem_path = os.path.join(base_dir, current_title)
        if not os.path.exists(problem_path):
            return current_title, problem_path

        print(f"文件夹已存在: {problem_path}")
        new_title = input("请输入新的题目名称: ").strip()
        if not new_title:
            print("名称不能为空，请重新输入。")
            continue
        current_title = new_title


def create_leetcode_problem():
    # 从剪贴板识别题目信息后，创建题目目录与两个模板文件。
    title, link = get_problem_from_clipboard()
    print(f"已识别题目: {title}")
    print(f"已识别链接: {link}")

    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    base_dir = os.path.join(project_root, "LeetCode")
    title, problem_path = resolve_problem_path(base_dir, title)

    os.makedirs(problem_path, exist_ok=True)
    print(f"已创建文件夹: {problem_path}")

    py_file = os.path.join(problem_path, "Solution.py")
    if not os.path.exists(py_file):
        with open(py_file, "w", encoding="utf-8") as file:
            file.write(f"# {link}\n\n\n")
            file.write("class Solution:\n")
            file.write("    pass\n")
        print("已创建代码文件: Solution.py")

    md_file = os.path.join(problem_path, "README.md")
    if not os.path.exists(md_file):
        with open(md_file, "w", encoding="utf-8") as file:
            file.write(f"# {title}\n\n")
            file.write(f"[题目链接]({link})\n\n")
            file.write("---\n\n")
            file.write("解题思路：\n")
        print("已创建说明文件: README.md")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    create_leetcode_problem()
