import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static FastIO io = new FastIO();

    static void solve() {
        // 这里写解题代码
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