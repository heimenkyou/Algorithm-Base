import java.io.*;
import java.math.BigInteger;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static FastIO io = new FastIO();

    // 在排好序的数组里，差值小于等于 x 的对子，一共有多少个
    private static long countLt(int x, int[] a) {
        long cnt = 0;
        int l = 0;
        for (int r = 0; r < a.length; r++) {
            while (a[r] - a[l] > x) {
                l++;
            }
            cnt += (r - l);
        }
        return cnt;
    }

    static void solve() {
        int n = io.nextInt();
        long k = io.nextLong();

        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = io.nextInt();
        }

        Arrays.sort(a);

        int l = 0, r = 100000000;
        int D = r;

        // 1. 通过二分找到第 k 大的差值 D
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (countLt(mid, a) >= k) {
                r = mid - 1;
                D = mid;
            } else {
                l = mid + 1;
            }
        }

        // 拿到D后，计算所有差值小于D的对子的和
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + a[i];
        }

        // 2. 双指针计算
        BigInteger ans = BigInteger.ZERO;
        long cnt = 0;
        int left = 0;

        for (int right = 0; right < n; right++) {
            while (left < right && a[right] - a[left] >= D) {
                left++;
            }
            long currentPairs = right - left;
            cnt += currentPairs;

            long term = currentPairs * a[right] - (prefix[right] - prefix[left]);
            ans = ans.add(BigInteger.valueOf(term));
        }

        // 可能个数不够 k 个，直接拿等于 D 的补齐
        long remCount = k - cnt;
        BigInteger rem = BigInteger.valueOf(remCount).multiply(BigInteger.valueOf(D));
        ans = ans.add(rem);

        io.println(ans.toString());
    }

    public static void main(String[] args) {
        int t = 1;
        // t = io.nextInt(); // 读入测试数据组数
        while (t-- > 0) {
            solve();
        }
        io.flush();
    }
}

class FastIO extends PrintWriter {
    private BufferedReader br;
    private StringTokenizer st;

    public FastIO() {
        // 包装 BufferedWriter 以获得更快的输出性能
        super(new BufferedWriter(new OutputStreamWriter(System.out)));
        br = new BufferedReader(new InputStreamReader(System.in));
    }

    // 判断并预读取下一个 token
    public boolean hasNext() {
        try {
            while (st == null || !st.hasMoreElements()) {
                String s = br.readLine();
                if (s == null)
                    return false;
                st = new StringTokenizer(s);
            }
        } catch (IOException e) {
            return false;
        }
        return true;
    }

    // 获取下一个字符串
    public String next() {
        return hasNext() ? st.nextToken() : null;
    }

    // 获取整数
    public int nextInt() {
        return Integer.parseInt(next());
    }

    // 获取长整数
    public long nextLong() {
        return Long.parseLong(next());
    }

    // 获取浮点数
    public double nextDouble() {
        return Double.parseDouble(next());
    }

    // 获取整行（会清空当前 Tokenizer 缓存，读取物理意义上的下一行）
    public String nextLine() {
        st = null;
        try {
            return br.readLine();
        } catch (IOException e) {
            return null;
        }
    }
}