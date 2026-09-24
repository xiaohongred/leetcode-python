class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        题意：找出不含重复字符的**最长子串**的长度（子串必须连续）。

        思路：不定长滑动窗口（同向双指针）
        - 窗口 [left, right] 始终保持「窗口内没有重复字符」这个性质。
        - right 向右扩张，把新字符 ch 纳入窗口。
        - 如果 ch 已经在窗口里，加入后就会出现重复，于是从左边不断移出字符，
          直到窗口里不再有 ch 为止。
        - 收缩结束后再把 ch 加进去，窗口重新合法，用窗口长度更新答案。

        关键点：为什么 while 里只判断 ch 一个字符？
        因为加入 ch 之前窗口是无重复的，那么产生重复的唯一来源只能是 ch 自己。
        所以只要把窗口里原有的那个 ch 挤出去，窗口就恢复合法。

        时间复杂度 O(n)：right 走一遍，left 总共也最多移动 n 步。
        空间复杂度 O(min(n, |Σ|))：window 集合最多装下字符集大小（|Σ| 为字符种类数）。
        """
        window = set()   # 当前窗口内出现的字符集合，用哈希在 O(1) 时间判断有没有重复
        left = 0         # 窗口左边界（包含）
        ans = 0          # 记录出现过的最长合法窗口长度

        # right 是窗口右边界，ch 是刚进入窗口的新字符
        for right, ch in enumerate(s):
            # ch 已在窗口中 -> 加入就重复，收缩左边界，直到 ch 被移出窗口
            while ch in window:
                window.remove(s[left])   # 左端字符离开窗口
                left += 1                # 左边界右移

            # 此时窗口内一定没有 ch，加入后仍然无重复
            window.add(ch)

            # 窗口 [left, right] 合法，长度为 right - left + 1
            ans = max(ans, right - left + 1)

        return ans


if __name__ == "__main__":
    solution = Solution()

    s = "abcabcbb"
    result = solution.lengthOfLongestSubstring(s)
    print(result)  # Output: 3   （"abc"，窗口在遇到第二个 'a' 时收缩）

    s = "bbbbb"
    result = solution.lengthOfLongestSubstring(s)
    print(result)  # Output: 1   （"b"，每来一个 b 都要把上一个 b 挤出去）

    s = "pwwkew"
    result = solution.lengthOfLongestSubstring(s)
    print(result)  # Output: 3   （"wke"，注意不是 "pwke"，因为子串必须连续）