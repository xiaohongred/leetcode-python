class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        """
        题意：找出最长的子串，使得子串中**每个字符的出现次数都不超过 2 次**。

        思路：不定长滑动窗口（同向双指针）+ 计数数组
        - 窗口 [left, right] 始终保持「每个字符出现次数 <= 2」这个性质。
        - 用 cnt[26] 统计窗口内 'a'~'z' 各自的个数。
        - right 向右扩张，把 s[right] 计入 cnt。
        - 收缩时 while 只需判断刚加入的那个字符 cnt[idx] > 2：
          因为加入 ch 之前窗口是合法的，超标的唯一来源就是 ch 自己，
          所以只要把左端字符不断移出，直到 ch 的计数降回 2 即可。

        和 LeetCode 3（无重复字符的最长子串）是同一套模板：
        那题是「每个字符最多出现 1 次」，这里是「每个字符最多出现 2 次」。

        时间复杂度 O(n)：right 走一遍，left 总共也最多移动 n 步。
        空间复杂度 O(1)：cnt 固定 26 个元素。
        """
        cnt = [0] * 26   # 窗口内 'a'~'z' 各自出现的次数
        left = 0         # 窗口左边界（包含）
        ans = 0          # 记录出现过的最长合法窗口长度

        for right, ch in enumerate(s):
            idx = ord(ch) - ord('a')   # 把字符映射为 0~25 的下标
            cnt[idx] += 1              # 新字符进入窗口，计数 +1

            # 该字符出现次数超过 2 -> 窗口不合法，从左边收缩
            while cnt[idx] > 2:
                cnt[ord(s[left]) - ord('a')] -= 1   # 左端字符离开窗口，计数 -1
                left += 1                           # 左边界右移

            # 窗口 [left, right] 合法，用长度更新答案
            ans = max(ans, right - left + 1)

        return ans


if __name__ == "__main__":
    solution = Solution()

    s = "bcbbbcba"
    result = solution.maximumLengthSubstring(s)
    print(result)  # Output: 4   （"bcba"；含 3 个 b 的窗口都不合法）

    s = "aaaa"
    result = solution.maximumLengthSubstring(s)
    print(result)  # Output: 2   （"aa"；第 3 个 a 进来时就要把第 1 个 a 挤出去）

    s = "aaabbbccc"
    result = solution.maximumLengthSubstring(s)
    print(result)  # Output: 4   （"aabb" 或 "bbcc"）