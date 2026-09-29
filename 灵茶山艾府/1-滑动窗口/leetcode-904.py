from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # 滑动窗口：窗口内水果种类 <= 2，求最长窗口
        cnt = {}
        ans = 0
        left = 0
        for right, f in enumerate(fruits):
            cnt[f] = cnt.get(f, 0) + 1
            while len(cnt) > 2:                  # 种类超了，收缩左边界
                x = fruits[left]
                cnt[x] -= 1
                if cnt[x] == 0:
                    del cnt[x]
                left += 1
            ans = max(ans, right - left + 1)
        return ans

    def totalFruitV2(self, fruits: List[int]) -> int:
        # 只记录两种水果各自最后出现的下标；出现第 3 种时，
        # 直接把左边界跳到「最后出现位置更靠前」的那种水果的下一位
        ans = 0
        left = 0
        last = {}                                # 窗口内水果种类 -> 最后出现下标
        for right, f in enumerate(fruits):
            last[f] = right
            if len(last) > 2:
                old = min(last, key=last.get)    # 最久没出现的那种
                left = last.pop(old) + 1
            ans = max(ans, right - left + 1)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.totalFruit([1,2,1]))  # 3
    print(s.totalFruit([0,1,2,2]))  # 3
    print(s.totalFruit([1,2,3,2,2]))  # 4
    print(s.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))  # 5
    print(s.totalFruitV2([1,2,1]))  # 3
    print(s.totalFruitV2([0,1,2,2]))  # 3
    print(s.totalFruitV2([1,2,3,2,2]))  # 4
    print(s.totalFruitV2([3,3,3,1,2,1,1,2,3,3,4]))  # 5