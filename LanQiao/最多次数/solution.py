# https://www.lanqiao.cn/problems/20542/learning/

import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

def get_next(s, start):
    ans = 10**18
    targets = ['lqb', 'lbq', 'qlb', 'qbl', 'blq', 'bql']
    found = False
    for t in targets:
        # if (pos := s.find(t, start)) != -1:
        pos = s.find(t, start)
        if pos != -1:
            if pos < ans:
                ans = pos
            found = True
            
    return int(ans) if found else -1

def main():
    line = input().strip()
    res = 0
    start = 0
    while True:
        # if (pos := get_next(line, start)) != -1:
        pos = get_next(line, start)
        if pos == -1:
            break
        res += 1
        start = pos + 3
    print(res)

if __name__ == '__main__':
    main()
