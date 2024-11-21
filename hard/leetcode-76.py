class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        res, resLen = [-1, -1], float("inf")
        l = 0
        have, need = 0, len(countT)
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                # 只有在 window[c] == countT[c] 时才对 have +1
                # 其他情况对 window[c] = 1 + window.get(c, 0) , 对于同一个字符，多次出现，只会在第一次满足条件时对 have +1
                have += 1

            while have == need:  # 注意这里用的 while, 每次只要满足  have == need 条件,就对l +1,缩小窗口
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop from the left of our window
                window[s[l]] -= 1  # 缩小窗口
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1  # l 右移 缩小窗口
        l, r = res
        return s[l:r + 1] if resLen != float("inf") else ""


if __name__ == '__main__':
    solu = Solution()

    s = "ADOBECODEBANC"
    t = "ABC"
    a = solu.minWindow(s, t)
    print(a)

    s = "a"
    t = "a"
    a = solu.minWindow(s, t)
    print(a)

    s = "a"
    t = "aa"
    a = solu.minWindow(s, t)
    print(a)
