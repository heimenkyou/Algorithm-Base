import sys
import time
import os
import gc

# 尝试导入绘图相关库
try:
    import matplotlib.pyplot as plt
    import pandas as pd
    HAS_VISUAL_LIBS = True
except ImportError:
    HAS_VISUAL_LIBS = False

# 快速 print：减少了 print 内部复杂的逻辑判断和动态转换
def fast_print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)) + end)

# 官方原版 print
def normal_print(*args, sep=' ', end='\n'):
    print(*args, sep=sep, end=end)

def test_performance():
    # 数据规模：从 1 到 100万
    scales = [1, 10, 100, 1000, 10000, 100000, 500000, 1000000]
    results = []

    # 准备测试数据 (模拟多参数输出)
    max_n = max(scales)
    test_data = [(i, 'test', i * 1.5) for i in range(max_n)]

    print(f"Python 版本: {sys.version.split()[0]}")
    print(f"{'Scale':<10} | {'Normal Print':<15} | {'Fast Print':<15} | {'Speedup':<10}")
    print('-' * 60)

    # 获取当前平台的黑洞设备
    null_device = os.devnull

    for n in scales:
        save_stdout = sys.stdout
        
        # --- 1. 测试原生 print ---
        with open(null_device, 'w') as f:
            sys.stdout = f
            gc.collect() # 减少 GC 干扰
            start = time.perf_counter()
            for i in range(n):
                normal_print(test_data[i][0], test_data[i][1], test_data[i][2])
            end_normal = time.perf_counter() - start
        
        # --- 2. 测试自定义 fast_print ---
        with open(null_device, 'w') as f:
            sys.stdout = f
            gc.collect()
            start = time.perf_counter()
            for i in range(n):
                fast_print(test_data[i][0], test_data[i][1], test_data[i][2])
            end_fast = time.perf_counter() - start

        # 还原 stdout
        sys.stdout = save_stdout

        speedup = end_normal / end_fast
        results.append({
            "Scale": n,
            "Normal": end_normal,
            "Fast": end_fast,
            "Speedup": speedup
        })

        print(f"{n:<10,d} | {end_normal:>13.8f}s | {end_fast:>13.8f}s | {speedup:>9.2f}x")

    return results

def show_chart(results):
    if not HAS_VISUAL_LIBS:
        print("\n[提示] 未检测到 matplotlib/pandas。")
        print("安装命令: pip install matplotlib pandas")
        return

    df = pd.DataFrame(results)
    
    plt.figure(figsize=(12, 6))
    
    # 左图：耗时对比
    plt.subplot(1, 2, 1)
    plt.plot(df["Scale"], df["Normal"], 'r-o', label='Normal Print')
    plt.plot(df["Scale"], df["Fast"], 'b-s', label='Fast Print (sys.stdout.write)')
    plt.xscale('log')
    plt.yscale('log')
    plt.title("Time Consumption (Log-Log Scale)")
    plt.xlabel("Scale (N)")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True, which="both", ls="--", alpha=0.5)

    # 右图：加速比
    plt.subplot(1, 2, 2)
    plt.plot(df["Scale"], df["Speedup"], 'g-^', label='Speedup Factor')
    plt.xscale('log')
    plt.axhline(y=1, color='r', linestyle='--')
    plt.title("Speedup: Fast vs Normal")
    plt.xlabel("Scale (N)")
    plt.ylabel("Multiplier (x faster)")
    plt.legend()
    plt.grid(True, which="both", ls="--", alpha=0.5)

    plt.tight_layout()
    print("\n正在生成可视化图表...")
    plt.show()

if __name__ == '__main__':
    bench_results = test_performance()
    show_chart(bench_results)