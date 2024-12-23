from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        stickCount = []  # stickCount[i] 存放的是一个字典，字典中包含了 stickers[i] 单词中每个字母的个数
        for i, s in enumerate(stickers):
            stickCount.append({})
            for c in s:
                stickCount[i][c] = 1 + stickCount[i].get(c, 0)

        dp = {}  # key = subseq of target | val = min num of stickers

        def dfs(t, stick):  # t 是需要拼接的目标字符串， stick 是纸片(纸片上包含字母的字典)
            if t in dp:
                return dp[t]

            res = 1 if stick else 0
            remainT = ""
            for c in t:  # 遍历 t  中每一个字母，看是否能在 stick 字典中找到, 第一次调用时 stick 为空
                if c in stick and stick[c] > 0:
                    stick[c] -= 1
                else:
                    remainT += c

            if remainT:  # 第一次调用时 remainT = target, 因为 上面 stick 为空
                # 最后一次调用时，t 不为空，stick 不为空，但经过上面的  for c in t 之后，remainT 为空了
                # 就不会进入到这个条件语句中，res 就是 1， 因为用了 stick 这个纸片
                used = float("inf")
                for s in stickCount:  # 尝试选择每一个 stickCount 中的字典(可选纸片)
                    if remainT[0] not in s:  # 为什么判断第一个字母就行
                        continue
                    used = min(used, dfs(remainT, s.copy()))
                dp[remainT] = used
                res += used
            return res

        res = dfs(target, {})
        return res if res != float('inf') else -1


if __name__ == '__main__':
    s = Solution()
    stickers = ["with", "example", "science"]
    target = "thehat"
    a = s.minStickers(stickers, target)
    print(a)

    stickers = ["notice", "possible"]
    target = "basicbasic"
    a = s.minStickers(stickers, target)
    print(a)
