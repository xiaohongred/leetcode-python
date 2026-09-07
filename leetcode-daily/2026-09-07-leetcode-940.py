class Solution:
    def distinctSubseqII(self, s: str) -> int:
        res = set()

        def dfs(i, path):
            if i == len(s):
                res.add(path)
                return
            # 选择当前字符
            dfs(i + 1, path + s[i])
            # 不选择当前字符
            dfs(i + 1, path)
        dfs(0, "")
        return len(res) - 1  # 减去空子序列的计数

    def distinctSubseqII_v2(self, s: str) -> int:
        n = len(s)
        # dp[i] 表示 s 的前 i 个字符能组成的不同子序列数量，包含空子序列。
        dp = [0] * (n + 1)
        dp[0] = 1  # 空子序列

        # 记录每个字符最近一次出现的位置，位置从 1 开始计数。
        last_occurrence = {}

        for i in range(1, n + 1):
            # 当前字符可以选择加入或不加入已有子序列，因此数量先翻倍。
            dp[i] = 2 * dp[i - 1]  # 每个子序列可以选择或不选择当前字符
            if s[i - 1] in last_occurrence:
                # 当前字符之前出现过，追加它会重新生成一部分重复子序列。
                j = last_occurrence[s[i - 1]]
                # 上次出现该字符时，前 j - 1 个字符形成的每个子序列
                # 都已经追加过这个字符；本次追加会再次生成它们。
                # 例如处理 "aba" 的最后一个 a 时，dp[2] = 4，
                # 先得到 2 * 4 = 8；第一次 a 在位置 1，
                # 所以 j = 1，需要减去 dp[j - 1] = dp[0] = 1，
                # 其中重复的子序列是 "a"，最终 dp[3] = 7。
                dp[i] -= dp[j - 1]
            last_occurrence[s[i - 1]] = i

        # 题目不计算空子序列，并按题目要求取模。
        return (dp[n] - 1) % (10**9 + 7)  # 减去空子序列的计数

    def distinctSubseqII_v3(self, s: str) -> int:
        n = len(s)
        # prev[i]：字符 s[i-1] 上一次出现的位置（1 基），若未出现过则为 0。
        prev = [0] * (n + 1)
        # solve(n) 的递归缓存，-1 表示还没计算过。
        dp = [-1] * (n + 1)
        lastSeen = [0] * 26  # 用于记录每个字符上一次出现的位置
        for i in range(1, n + 1):
            idx = ord(s[i - 1]) - ord('a')

            # 记录当前字符上一次出现的位置，再更新 lastSeen。
            prev[i] = lastSeen[idx]
            lastSeen[idx] = i
        
        def solve(n):
            # solve(n) 表示 s 的前 n 个字符能组成的不同子序列数量（含空子序列）。
            if n == 0:
                return 1
            if dp[n] != -1:
                return dp[n]
            # 每个已有子序列都可以选择加入或不加入当前字符，所以先翻倍。
            total = (2 * solve(n - 1)) % (10**9 + 7)
            if prev[n] != 0:
                # 当前字符之前出现过，本次追加会重复生成 solve(prev[n] - 1) 个旧结果。
                duplicates = solve(prev[n] - 1)
                total = (total - duplicates) % (10**9 + 7)

            dp[n] = total
            return total
        # solve(n) 含空子序列，题目不统计空子序列，因此减 1。
        return (solve(n) - 1) % (10**9 + 7)  # 减去空子序列的计数
if __name__ == "__main__":
    solution = Solution()

    # 测试用例：每个元素为 (s, 期望结果)。
    test_cases = [
        ("abc", 7),
        ("aba", 6),
        ("aaa", 3),
    ]

    # 依次测试三种实现。
    for method_name in ["distinctSubseqII", "distinctSubseqII_v2", "distinctSubseqII_v3"]:
        method = getattr(solution, method_name)
        for s, expected in test_cases:
            result = method(s)
            status = "OK" if result == expected else "FAIL"
            print(f"{method_name}({s!r}) = {result}  (期望 {expected})  [{status}]")
            assert result == expected, (method_name, s, result, expected)