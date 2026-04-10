# https://www.luogu.com.cn/problem/P1305

import sys

input = sys.stdin.readline

def main():
    n = int(input())
    left = [0] * 30
    right = [0] * 30
    root = 0
    for i in range(n):
        # 转成字母表的顺序即 c='a'
        node, l, r = [
            ord(c) - ord('a') + 1 if c != '*' else c
            for c in input().strip()
        ]
        if l != '*': left[node] = l
        if r != '*': right[node] = r
        if i == 0: root = node

    res = []
    def preorder(root):
        if root == 0: return
        res.append(chr(root + ord('a') - 1))
        preorder(left[root])
        preorder(right[root])

    preorder(root)
    print(''.join(res))

if __name__ == '__main__':
    main()
