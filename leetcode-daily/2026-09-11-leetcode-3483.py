from typing import List
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # 暴力枚举下标：i 百位、j 十位、k 个位，set 去重。时间 O(n^3)
        n = len(digits)
        seen = set()
        for i in range(n):
            if digits[i] == 0:            # 不能有前导零
                continue
            for j in range(n):
                if j == i:                # 每个下标只能用一次
                    continue
                for k in range(n):
                    if k == i or k == j:  # 三个下标互不相同
                        continue
                    if digits[k] % 2:     # 个位必须是偶数
                        continue
                    seen.add(digits[i] * 100 + digits[j] * 10 + digits[k])
        return len(seen)

    def totalNumbersV2(self, digits: List[int]) -> int:
        # 记剩余个数，按 个位 -> 百位 -> 十位 枚举，时间 O(10^3)
        cnt = [0] * 10
        for d in digits:
            cnt[d] += 1        # 数字可以重复用，前提是数组里有多个

        ans = 0
        for unit in range(0, 10, 2):        # 个位：0,2,4,6,8
            if cnt[unit] == 0:
                continue
            cnt[unit] -= 1                  # 用掉一个个位数字
            for hundred in range(1, 10):    # 百位：1~9，不能为 0
                if cnt[hundred] == 0:
                    continue
                cnt[hundred] -= 1           # 用掉一个百位数字
                ans += sum(1 for t in range(10) if cnt[t] > 0)  # 十位任取剩余数字
                cnt[hundred] += 1           # 回溯
            cnt[unit] += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    cases = [
        ([1, 2, 3, 4], 12),
        ([0, 2, 2], 2),
        ([6, 6, 6], 1),
        ([1, 3, 5], 0),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 328),
    ]
    for digits, expected in cases:
        got1 = s.totalNumbers(digits)
        got2 = s.totalNumbersV2(digits)
        print(f"{digits} -> {got1}, {got2} (expected {expected})",
              "OK" if got1 == got2 == expected else "FAIL")