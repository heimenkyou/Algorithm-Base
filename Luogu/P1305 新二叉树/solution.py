# https://www.luogu.com.cn/problem/P1305

import sys

input = sys.stdin.readline

def main():
    n = int(input())
    left = {}
    right = {}
    root = 0
    for i in range(n):
        # 转成字母表的顺序即 c='a'
        node, l, r = input().strip()
        if l != '*': left[node] = l
        if r != '*': right[node] = r
        if i == 0: root = node

    res = []
    def preorder(root):
        if root == '*': return
        res.append(root)
        preorder(left.get(root, '*'))
        preorder(right.get(root, '*'))

    preorder(root)
    print(''.join(res))

if __name__ == '__main__':
    main()
