class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # 滑动窗口：窗口内每个字符出现次数 <= 2
        cnt = [0] * 26
        ans = 0
        left = 0
        for right, ch in enumerate(s):
            c = ord(ch) - ord('a')
            cnt[c] += 1
            while cnt[c] > 2:            # 只有新加入的字符可能超过 2 次
                cnt[ord(s[left]) - ord('a')] -= 1
                left += 1                # 收缩左边界直到合法
            ans = max(ans, right - left + 1)
        return ans

if __name__ == "__main__":
    s = "bcbbbcba"
    solution = Solution()
    print(solution.maximumLengthSubstring(s))  # 4

    s = "aaaa"
    solution = Solution()
    print(solution.maximumLengthSubstring(s))  # 2