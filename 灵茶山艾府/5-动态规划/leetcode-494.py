from functools import cache


def zero_one_knapsack_dfs(weights, values, capacity):
    n = len(weights)

    @cache
    def dfs(i, c):
        if i < 0:
            return 0
        if weights[i] > c:
            return dfs(i - 1, c)
        return max(dfs(i - 1, c), dfs(i - 1, c - weights[i]) + values[i])
    return dfs(n - 1, capacity)

def zero_one_knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        """
        写法一：记忆化搜索（自顶向下）。

        ── 第一步：把「填加减号」转化成「选子集」 ──────────────────────────
        设 s = sum(nums)（所有数的总和），
           p = 被填上 '+' 号的那些数的和，
           q = 被填上 '-' 号的那些数的和（也就是注释里的 s - p）。

        那么一定有：
            p + q = s       每个数要么进 p、要么进 q，正好把 s 分完
            p - q = target  因为最终表达式的值就是所有 '+' 项减所有 '-' 项
        两式相加，消掉 q：
            2p = s + target
            p  = (s + target) / 2

        于是原问题等价于：**从 nums 中挑出一个子集，让它的和恰好等于 (s + target)/2**。
        挑出来的这些数填 '+'，剩下的填 '-'，就能凑出 target；反之每个合法的符号方案
        也唯一对应这样一个子集。两者是一一对应的，所以「数符号方案数」= 「数子集方案数」。

        有两个前提，只要有一条不满足就直接无解、返回 0：
            * s + target 必须是偶数，否则 p 不是整数；
            * p 必须非负，即 s + target >= 0（nums 全非负时 s >= 0，所以等价于 target >= -s）。

        ── 第二步：数方案数 ──────────────────────────────────────────────
        问题化为经典的「子集和计数」：从 nums 中选若干个数，和为 p 的方案数。
        注意：下面把参数 target 原地改写成了 s + target，再整除 2 得到 p，
        所以函数后半段的 target 已经不是题目给的那个 target 了，读的时候要留个心。
        """
        target += sum(nums)  # 此时 target = s + target(原值)
        if target < 0 or target % 2:
            return 0  # 负数（p < 0）或奇数（p 不是整数），无解

        target = target // 2  # 此时 target = p，即子集和的目标值

        n = len(nums)

        @cache
        def dfs(i, c):
            """
            返回：从 nums[0..i]（含下标 i）中选若干个互不相同的数，每个数最多用一次，
                  使其和恰好等于 c 的方案数。

            i：当前正在做决定的下标，从 n-1 开始一路往前推
            c：还需要凑出的剩余和

            注意递归终点是 i < 0（所有数都考虑完了），而不是 i == 0。
            """
            if i < 0:
                # 没有数可选了：只有「剩余和刚好为 0」才算成功凑出一种方案，
                # 否则这条路是失败的，记 0 种。
                return 1 if c == 0 else 0
            if c < nums[i]:
                # 剩余和比 nums[i] 还小，nums[i] 一旦选就会超标，所以只能不选
                return dfs(i - 1, c)
            # nums[i] 有两种命运，两条路的方案数相加：
            #   不选 nums[i]：还得从 nums[0..i-1] 里凑出 c
            #   选   nums[i]：还得从 nums[0..i-1] 里凑出 c - nums[i]
            return dfs(i - 1, c) + dfs(i - 1, c - nums[i])  # 选或不选 nums[i]，两种情况相加

        # 问题已转化为：从 nums 中选一些数，使其和为 target（即 p），问有多少种选法
        return dfs(n - 1, target)

    def findTargetSumWaysDp(self, nums: list[int], target: int) -> int:
        """
        写法二：递推（自底向上填表）。

        转化过程和 「p = (s + target)/2」的推导与 findTargetSumWays 完全一样，
        区别只是把记忆化搜索 dfs(i, c) 换成了按顺序填一张二维表 f。
        对应关系：f[i][c] <==> dfs(i - 1, c)。（dfs 的下标 i 是「包含 i」，
        表的下标 i 是「考虑了前 i 个数」，两者相差 1。）
        """
        target += sum(nums)          # 此时 target = s + target(原值)
        if target < 0 or target % 2:
            return 0                 # p 为负或不是整数，无解
        target = target // 2         # 此后 target 表示子集和的目标值 p

        n = len(nums)

        # ══════════════════════════════════════════════════════════════════
        # f[i][c] 的含义：
        #
        #   从 nums 的「前 i 个数」——也就是 nums[0], nums[1], ..., nums[i-1] ——
        #   中选出若干个互不相同的数（每个数最多用一次），
        #   使它们的和「恰好等于 c」的方案数。
        #
        #   行 i：0 <= i <= n，表示「考虑了前 i 个数」（i = 0 表示一个数都还没考虑）
        #   列 c：0 <= c <= target，表示要凑出的和
        #   值  ：方案数（选法个数），只统计「恰好等于 c」的那些选法
        #
        #   特别注意「恰好」两个字：和小于 c 的选法不算，和大于 c 的选法也不算。
        #   因此 f 的值只由「能否正好凑出来」决定，和 0-1 背包求最大值是完全不同的语义。
        #
        #   与上面 dfs 的对应关系：
        #       f[i][c]  <==>  dfs(i - 1, c)      （dfs 的 i 是包含 i，这里差 1）
        # ══════════════════════════════════════════════════════════════════
        f = [[0] * (target + 1) for _ in range(n + 1)]

        # 边界：f[0][0] = 1。
        # 「前 0 个数」凑出和 0：唯一的办法是什么都不选（空集），所以方案数是 1。
        # 而 f[0][c] (c > 0) 保持默认的 0：一个数都没有，凑不出正数和。
        f[0][0] = 1  # 初始化，选 0 个数，凑出和为 0 有 1 种方案

        for i, x in enumerate(nums):  # x = nums[i]，用「前 i 个数」推出「前 i+1 个数」
            for c in range(target + 1):
                # 决策一：不选 x，方案数直接继承「前 i 个数凑出 c」的方案数
                f[i + 1][c] = f[i][c]
                # 决策二：选 x，则剩下的 c - x 必须由前 i 个数凑出来，
                #         所以要求 c >= x（否则 x 比需要的和还大，选了就超标）
                if c >= x:
                    f[i + 1][c] += f[i][c - x]
                # 两种决策互斥（x 要么选要么不选），方案数相加，
                # 与 dfs 里那句 `return dfs(i-1, c) + dfs(i-1, c-nums[i])` 一一对应。
                #
                # 顺带一提：列范围只开到 target，所以「中途和就超过 target」的选法
                # 被自动排除在外。这不会漏解 —— nums 非负，和一旦超过 target 就
                # 再也降不回来，不可能最终恰好等于 target。
                #
                # 优化提示：f 的每一行只依赖上一行，可压缩成一维数组，
                # 并把内层循环改成从 target 倒序到 x（正序会让同一个 x 被重复使用），
                # 与文件顶部 zero_one_knapsack 的滚动数组写法是同一个套路。

        # 答案：考虑完所有 n 个数后，恰好凑出 target 的方案数
        return f[n][target]

    def findTargetSumWaysDpSaveMem(self, nums: list[int], target: int) -> int:
        """
        写法三：二维表 + 滚动数组（只保留相邻两行）。

        转化过程（p = (s + target)/2）与 findTargetSumWays 完全一样，这里不再重复。
        本版只优化「空间」：写法二的 f 开了 (n+1) 行，但算 f[i+1] 时只读 f[i]，
        再往前的行永远用不到了，所以留两行轮流用就够 ——
        用 i % 2 和 (i+1) % 2 分别指着「上一行」和「当前行」，
        空间从 O(n · target) 降到 O(2 · target) = O(target)。
        """
        target += sum(nums)          # 此时 target = s + target(原值)
        if target < 0 or target % 2:
            return 0                 # p 为负或不是整数，无解
        target = target // 2         # 此后 target 表示子集和的目标值 p

        n = len(nums)

        # 两行轮流使用：
        #   处理第 i 个数时，f[i % 2]      <- 相当于写法二的 f[i]     （上一行，只读）
        #                f[(i + 1) % 2]  <- 相当于写法二的 f[i + 1] （当前行，只写）
        # 注意「读的行」和「写的行」是两个不同的行，这一点决定了内层循环可以正序遍历。
        f = [[0] * (target + 1) for _ in range(2)]

        # 边界：前 0 个数凑出和 0 有 1 种方案（空集），即写法二的 f[0][0] = 1
        f[0][0] = 1  # 初始化，选 0 个数，凑出和为 0 有 1 种方案

        for i, x in enumerate(nums):  # x = nums[i]，用「前 i 个数」推出「前 i+1 个数」
            for c in range(target + 1):
                # 决策一：不选 x —— 继承上一行的同列值
                f[(i + 1) % 2][c] = f[i % 2][c]
                # 决策二：选 x —— 需要上一行凑出 c - x，所以要求 c >= x
                if c >= x:
                    f[(i + 1) % 2][c] += f[i % 2][c - x]
                # 关键点：这里写 (i+1) % 2 行、读 i % 2 行，两者是不同的一行，
                # 所以 c 正序还是倒序遍历，都不可能读到「本轮刚写进去的新值」，
                # 内层循环保持正序即可，不需要像写法四那样倒着走。
                #
                # 反过来说，如果连这一行都省掉、直接用 f[c] 就地更新（写法四），
                # 那「读的行」就等于「写的行」，就必须改成倒序了。

        # 答案：处理完 n 个数后，结果恰好停在 n % 2 这一行
        return f[(n) % 2][target]

    def findTargetSumWaysDpSaveMemV2(self, nums: list[int], target: int) -> int:
        """
        写法四：一维数组（在写法三的基础上再省掉一行）。

        思路：既然算 f[i+1] 只依赖 f[i]，干脆让「当前行」和「上一行」共用同一个数组，
        一边读一边就地更新。此时 f[c] 的含义是「随外层循环推进而变化」的：
            * 进入第 i 次外层循环之前：f[c] = f[i][c]    （前 i 个数凑出 c 的方案数）
            * 第 i 次外层循环结束之后：f[c] = f[i+1][c]  （前 i+1 个数凑出 c 的方案数）
            * 循环全部结束后：f[c] = f[n][c]，答案即 f[target]
        空间进一步降到一个长度 target + 1 的数组。

        转化过程（p = (s + target)/2）同样见 findTargetSumWays 的说明。
        """
        target += sum(nums)          # 此时 target = s + target(原值)
        if target < 0 or target % 2:
            return 0                 # p 为负或不是整数，无解
        target = target // 2         # 此后 target 表示子集和的目标值 p

        n = len(nums)                # 本题里 n 只是「数的个数」，下面直接 for x in nums，用不到它

        f = [0] * (target + 1)       # f[c] = 用「当前已处理过的那些数」凑出 c 的方案数
        f[0] = 1                     # 初始化，选 0 个数，凑出和为 0 有 1 种方案

        for x in nums:
            # ★ 必须倒序遍历：从 target 递减到 x
            #   （range(target, x - 1, -1) 的右端是开区间，所以真正做到取到 c = x）
            #
            # 为什么要倒序？本行是 f[c] += f[c - x]，等号右边的 f[c - x] 必须是
            # 「本轮还没被更新过」的旧值，也就是 f[i][c - x]：
            #   * 倒序：c 从大到小，去读 f[c - x] 时它一定还没被本轮碰过，拿到的正是旧值 ✔
            #   * 正序：c 从小到大，f[c - x] 早已被本轮更新过了，效果等于让 x 被重复使用，
            #           算出来就成了「每个数可无限次选取」的完全背包，答案会偏大 ✘
            #
            # 另外两点小细节：
            #   * 下界取到 x（而不是 0），等价于替我们做掉了二维版本里那句 `if c >= x`：
            #     c < x 时 f[c - x] 没有意义，直接不进循环。
            #   * x = 0 时范围是 range(target, -1, -1)，会走到 c = 0，执行 f[0] += f[0]，
            #     方案数翻倍 —— 这恰好对应「这个 0 选或不选」的两种选择，结果仍然正确。
            for c in range(target, x - 1, -1):
                f[c] += f[c - x]
        return f[target]

if __name__ == "__main__":
    weights = [1, 2, 3]
    values = [6, 10, 12]
    capacity = 5
    print(zero_one_knapsack_dfs(weights, values, capacity))  # 输出: 22
    print(zero_one_knapsack(weights, values, capacity))      # 输出: 22

    nums = [1, 1, 1, 1, 1]
    target = 3
    s = Solution()
    print(s.findTargetSumWays(nums, target))  # 输出: 5