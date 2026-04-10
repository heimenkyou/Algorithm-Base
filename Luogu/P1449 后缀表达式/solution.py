# https://www.luogu.com.cn/problem/P1449

import sys

input = sys.stdin.readline

def main():
    s = input().strip()

    stack = []
    num = 0
    for c in s:
        if c == '@':
            break
        # 处理数字读入
        if c.isdigit():
            num = num * 10 + ord(c) - ord('0')
        elif c == '.':
            stack.append(num)
            num = 0
        # 处理运算
        else:
            b = stack.pop()
            a = stack.pop()
            if c == '+':
                stack.append(a + b)
            elif c == '-':
                stack.append(a - b)
            elif c == '*':
                stack.append(a * b)
            elif c == '/':
                stack.append(a // b)
    print(stack.pop())
            

if __name__ == '__main__':
    main()
