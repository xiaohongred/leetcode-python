class Solution:
    """
    LeetCode 42. 接雨水（前缀 / 后缀最大值解法）

    给定一排宽度为 1 的柱子高度 height，求下雨后一共能接住多少单位雨水。
    例如 [0,1,0,2,1,0,1,3,2,1,2,1] -> 6，[4,2,0,3,2,5] -> 9。

    ── 核心物理直觉：每一列各自算自己能接多少水 ────────────────────────
    把每根柱子单独拿出来看，它上方能积多少水，只由左右两边「最高的挡板」决定：
        * 水会从缺口流走，而两侧挡板里较矮的那一侧就是缺口，
          所以位置 i 的水位 = min(它左边的最高柱子, 它右边的最高柱子)；
        * 柱子本身还占着高度 height[i]，所以真正积住的水 = 水位 - height[i]。
    把每一列的积水量加起来就是答案。

    ★ 一个小细节：pre_max[i] / suf_max[i] 都把 height[i] 自己算了进去
      （pre_max[i] = max(height[0..i])）。好处是 min(pre, suf) >= height[i] 天然成立，
      既不会算出负的积水量，第一个 / 最后一个位置也不用特判。

    复杂度：时间 O(n)（三趟扫描），空间 O(n)（两个辅助数组）。
    """

    def trap(self, height: list[int]) -> int:
        n = len(height)

        # 第 1 趟：前缀最大值。
        # pre_max[i] = max(height[0..i])，即「位置 i 以及它左边所有柱子里最高的那根」
        pre_max = [0] * n
        pre_max[0] = height[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i-1], height[i])

        # 第 2 趟：后缀最大值。
        # suf_max[i] = max(height[i..n-1])，即「位置 i 以及它右边所有柱子里最高的那根」
        suf_max = [0] * n
        suf_max[-1] = height[-1]
        for i in range(n-2, -1, -1):
            suf_max[i] = max(suf_max[i+1], height[i])

        # 第 3 趟：逐列结算。
        # 位置 i 的水位是两侧最高挡板里较矮的那个，再减去自身高度就是这一列积住的水。
        # zip 把三个数组同一下标的值绑在一起，写起来比下标循环清爽。
        ans = 0
        for h, pre, suf in zip(height, pre_max, suf_max):
            ans += (min(pre, suf) - h)
        return ans

    def trapV2(self, height: list[int]) -> int:
        """
        双指针版：和 trap 用的是同一个原理（水位 = min(左最高, 右最高) - 自身高），
        只是把两个辅助数组换成两个变量，空间从 O(n) 降到 O(1)。

        ── 关键问题：凭什么现在就敢结算某一列？ ────────────────────────────
        站在 left 这个位置看：
            * 左边的最高挡板 pre_max = max(height[0..left])，**已经确定**了；
            * 右边虽然还没扫完，但一定存在高度至少为 suf_max 的柱子
              （suf_max = max(height[right..n-1])，而位置 left 右边的真实最高值
                 = max(height[left..n-1]) 显然 >= suf_max）。
        于是有：
            * 若 pre_max < suf_max，那么 min(左边真正的最高, 右边真正的最高)
              = pre_max（因为右边至少是 suf_max，比 pre_max 更高），
              说明 **left 这一列的水位此刻就已经定下来了**，可以立刻结算，然后 left 右移；
            * 反之要是 pre_max >= suf_max，对称地可以确定 right 那一列的水位就是 suf_max，
              于是结算 right，然后 right 左移。

        也就是说：每一轮总能找到一个「已知的那一侧更矮」的位置可以安全结算，
        根本不需要提前把整条「左最高 / 右最高」数组都算出来。
        """
        n = len(height)

        ans = 0
        left = 0
        right = n - 1
        # pre_max = max(height[0..left])、suf_max = max(height[right..n-1])，
        # 都是「已经扫过的那些位置」里的最高挡板，循环开头会先各自推进一次。
        # 初值取 0 是依赖「height 中都是非负数」（题目保证）；
        # 若数组里可能有负数，这里就得改成 -inf。
        pre_max = 0
        suf_max = 0

        while left <= right:              # 两端相遇时还要处理中间那一列，所以用 <=
            # 先把两侧的最高挡板推进到包含 left / right 的位置
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])

            if pre_max < suf_max:
                # 左边的挡板更矮，短板在左边 -> left 的水位由 pre_max 决定
                ans += pre_max - height[left]
                left += 1                 # left 这一列结算完毕，右移
            else:
                # 右边更矮（或两边一样高，此时结算哪一侧都对，因为 min 相同）
                # -> right 的水位由 suf_max 决定
                ans += suf_max - height[right]
                right -= 1                # right 这一列结算完毕，左移

        # 每一轮恰好结算一列（left 或 right 二选一），所以循环正好跑 n 次：
        # 时间 O(n)，额外空间只有 4 个变量。
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
    print(s.trap([4,2,0,3,2,5]))              # 9


# =============================================================================
# 补充说明
# =============================================================================
#
# 1) 为什么水位是 min(左边最高, 右边最高)，而不是两者里较高的那个？
#    想象往位置 i 倒水：水会一直积到「最低的那个缺口」为止。
#    两侧挡板中较矮的一侧就是那个缺口，水面一旦超过它就会从那里流走，
#    所以最终水面高度恰好等于较矮的那块挡板的高度。
#
# 2) 为什么 pre / suf 都要把 height[i] 自己包含进去？
#    这样 min(pre_max[i], suf_max[i]) 一定 >= height[i]，
#    逐列相减时不可能出现负数，也不用为第一个 / 最后一个位置写特判。
#
# 3) 复杂度与进一步优化：
#    现在 trap 是「时间 O(n) + 空间 O(n)（两个数组）」。还能继续压：
#      * 省掉 suf_max：第一趟算完 pre_max 后，第二趟从右往左扫的同时用滚动变量
#        维护 suf，就能边扫边累加答案；
#      * 再进一步就是本文件里的 trapV2（双指针）：只用 pre_max / suf_max 两个变量，
#        每轮结算「已知的那一侧更矮」的那一列，空间降到 O(1)。
#        为什么这样结算是对的，见 trapV2 的 docstring。
#
# 4) 小提示：LeetCode 保证 height 长度至少为 1。若真传入空数组，
#    `pre_max[0] = height[0]` 会下标越界。
