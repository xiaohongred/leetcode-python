class Solution:
    def maxScore(self, s: str) -> int:
        total1 = s.count('1')  # 计算字符串中 '1' 的总数
        # total0 = s.count('0')  # 计算字符串中 '0' 的总数
        max_score = 0
        left0 = 0
        right1 = total1

        for i in range(len(s) - 1):
            if s[i] == '0':
                left0 += 1
            else:
                right1 -= 1
            max_score = max(max_score, left0 + right1)

        return max_score

if __name__ == "__main__":
    solution = Solution()
    s = "011101"
    result = solution.maxScore(s)
    print(result)  # Output: 5

    s = "00111"
    result = solution.maxScore(s)
    print(result)  # Output: 5

    s = "1111"
    result = solution.maxScore(s)
    print(result)  # Output: 3