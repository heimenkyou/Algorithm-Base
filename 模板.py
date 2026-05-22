import sys
import math
import heapq
from collections import defaultdict, deque, Counter
from functools import cache, lru_cache, cmp_to_key

# ================= 赛场环境与 I/O 配置 =================
# 1. 解除递归深度限制（树形DP、深层DFS、记忆化搜索必备）
sys.setrecursionlimit(200000)

# 2. 快速输入输出配置（按行读取）
input = sys.stdin.readline
def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)) + end)

# ================= 常用全局常量定义 =================
INF = float('inf')        # 正无穷大，用于求最小值时的初始化
MOD = 10**9 + 7           # 常用取模常数（有时是 998244353）
# DIRS = [(0,1), (1,0), (0,-1), (-1,0)] # 迷宫/网格图常用方向数组(右下左上)

# ================= 核心逻辑区 =================
def main():
    # ---------------- 常用读取模板 ----------------
    # 1. 读单个整数：
    # n = int(input())
    
    # 2. 读多个独立整数：
    # n, m = map(int, input().split())
    
    # 3. 读一行数组：
    # a = list(map(int, input().split()))
    
    # 4. 读多行矩阵/网格：
    # grid = [list(map(int, input().split())) for _ in range(n)]
    # ----------------------------------------------
    pass

if __name__ == '__main__':
    main()