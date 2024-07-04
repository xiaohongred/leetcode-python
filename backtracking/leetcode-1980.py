from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        strSet = {s for s in nums}
        li = []

        def backtrack(i, cur) -> str:
            if i == len(nums):
                res = "".join(cur)
                li.append(res)
                return None if res in strSet else res
            # cur[i] = "0"
            res = backtrack(i + 1, cur)
            if res:
                return res

            cur[i] = "1"
            res = backtrack(i + 1, cur)
            cur[i] = "0"  # 这一行不加也能AC
            if res:
                return res

        a = backtrack(0, ["0" for s in nums])
        print(li)
        return a


if __name__ == '__main__':
    nums = ["11", "00"]
    s = Solution()
    a = s.findDifferentBinaryString(nums)
    print(a)

    nums = ["011", "001", "000"]
    a = s.findDifferentBinaryString(nums)
    print(a)
