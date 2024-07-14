from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]

                if dp[i]:
                    break
        return dp[0]

    def wordBreakV2(self, s: str, wordDict: List[str]) -> bool:
        cache = {}

        def dfs(i):
            if i == len(s):
                return True

            if i in cache:
                return cache[i]
            for w in wordDict:
                wLen = len(w)
                if s[i:i + wLen] == w:
                    if dfs(i + wLen):
                        cache[i] = True
                        return True
            cache[i] = False
            return False

        return dfs(0)


if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]

    solu = Solution()

    a = solu.wordBreak(s, wordDict)
    print(a)
