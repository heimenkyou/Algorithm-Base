"""
批量补零 LeetCode 文件夹名称中的数字部分，使其达到 4 位。
需要在项目根目录下运行此脚本，确保 LeetCode 文件夹存在且包含需要处理的文件夹。
"""

import os
import re


def batch_pad_leetcode_digits():
    # 获取当前脚本所在目录，并定位到 LeetCode 文件夹
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.join(current_dir, 'LeetCode')

    if not os.path.exists(base_dir):
        print(f'未找到 LeetCode 目录，请检查路径: {base_dir}')
        return

    print('开始检查并重命名文件夹...')
    success_count = 0

    for folder_name in os.listdir(base_dir):
        dir_path = os.path.join(base_dir, folder_name)

        # 确保只处理文件夹
        if not os.path.isdir(dir_path):
            continue

        # 匹配以数字开头，紧跟一个点号的文件夹名称
        match = re.match(r'^(\d+)\.(.*)$', folder_name)
        if match:
            num_str, rest = match.groups()
            # 如果数字位数不足 4 位，则进行补零
            if len(num_str) < 4:
                new_num_str = num_str.zfill(4)
                new_folder_name = f'{new_num_str}.{rest}'
                new_dir_path = os.path.join(base_dir, new_folder_name)

                print(f'重命名: {folder_name} -> {new_folder_name}')
                os.rename(dir_path, new_dir_path)
                success_count += 1

    print(f'处理完成，共成功重命名 {success_count} 个文件夹。')


if __name__ == '__main__':
    batch_pad_leetcode_digits()
