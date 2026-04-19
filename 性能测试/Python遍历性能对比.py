import timeit
import gc
import sys

# 1. 尝试导入绘图相关库
try:
    import matplotlib.pyplot as plt
    import pandas as pd
    HAS_VISUAL_LIBS = True
except ImportError:
    HAS_VISUAL_LIBS = False

def run_benchmark():
    # 测试规模：1k 到 1M
    scales = [1_000, 10_000, 100_000, 1_000_000]
    results = []
    
    print(f"Python 版本: {sys.version.split()[0]}")
    print(f"{'数据规模':<12} | {'直接遍历':<12} | {'下标遍历':<12} | {'Enumerate':<12}")
    print("-" * 60)

    for n in scales:
        # 准备测试数据
        setup = f"data = list(range({n}))"
        
        # 显式清理内存，减少干扰
        gc.collect()
        
        # 测量直接遍历 (for x in data)
        t_direct = timeit.timeit("for x in data: pass", setup=setup, number=20) / 20
        
        # 测量下标遍历 (for i in range(len(data)))
        t_range = timeit.timeit("for i in range(len(data)): _ = data[i]", setup=setup, number=20) / 20
        
        # 测量 Enumerate (for i, x in enumerate(data))
        t_enumerate = timeit.timeit("for i, x in enumerate(data): pass", setup=setup, number=20) / 20
        
        results.append({
            "Scale": n,
            "Direct": t_direct,
            "Range": t_range,
            "Enumerate": t_enumerate
        })
        
        print(f"{n:<12,d} | {t_direct:10.6f}s | {t_range:10.6f}s | {t_enumerate:10.6f}s")
    
    return results

def show_chart(results):
    if not HAS_VISUAL_LIBS:
        print("\n[系统提示] 未检测到 matplotlib/pandas。")
        print("如需查看图表，请运行: pip install matplotlib pandas")
        return

    # 使用 pandas 处理数据
    df = pd.DataFrame(results)
    
    # 绘图逻辑
    plt.figure(figsize=(10, 6))
    plt.plot(df["Scale"], df["Direct"], marker='o', linestyle='-', label='Direct (for x in L)')
    plt.plot(df["Scale"], df["Range"], marker='s', linestyle='--', label='Range (L[i])')
    plt.plot(df["Scale"], df["Enumerate"], marker='^', linestyle='-.', label='Enumerate')

    # 设置对数坐标轴，方便跨数量级对比
    plt.xscale('log')
    plt.yscale('log')
    
    plt.title("Python Iteration Performance: Direct vs Range vs Enumerate", fontsize=14)
    plt.xlabel("Scale (N) - Log Scale", fontsize=12)
    plt.ylabel("Time (seconds) - Log Scale", fontsize=12)
    plt.legend()
    plt.grid(True, which="both", ls="--", alpha=0.5)
    
    print("\n正在展示图表...")
    plt.show()

if __name__ == "__main__":
    # 执行测试
    bench_data = run_benchmark()
    # 尝试绘图
    show_chart(bench_data)