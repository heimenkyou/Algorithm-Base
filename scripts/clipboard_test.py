"""
使用方法：
1. 复制力扣网站题目描述中的标题
2. 运行脚本

这个脚本只用来验证：
- 能否从剪贴板拿到题目标题
- 能否从剪贴板里的 HTML 提取出题目链接
"""

import ctypes
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


def get_problem_from_clipboard():
    # 纯文本里直接是题目标题。
    title = read_clipboard_bytes(CF_UNICODETEXT).decode("utf-16-le").rstrip("\x00").strip()

    # 力扣复制标题时，HTML 里会带有 href，可以直接提取题目链接。
    html_format = user32.RegisterClipboardFormatW("HTML Format")
    html = read_clipboard_bytes(html_format).decode("utf-8").rstrip("\x00")
    match = re.search(r'href="([^"]+)"', html)
    if not match:
        print("未识别到力扣题目链接，请先复制力扣题目描述中的标题。")
        print(f"当前剪贴板标题: {title or '<空>'}")
        preview = html[:200].replace("\n", "\\n")
        print(f"当前剪贴板 HTML 前 200 个字符: \n{preview or '<空>'}\n")
        raise ValueError("剪贴板中没有找到题目链接")

    link = match.group(1)
    return title, link


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    title, link = get_problem_from_clipboard()
    print("title:", title)
    print("link:", link)
