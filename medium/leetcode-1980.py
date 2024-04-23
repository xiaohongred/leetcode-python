from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        strSet = {s for s in nums}

        def backtrack(i, cur):
            if i == len(nums):
                res = "".join(cur)
                return None if res in strSet else res
            # cur[i] = "0" 这个操作可以省略
            res = backtrack(i + 1, cur)
            if res:
                return res
            
            # res is None
            cur[i] = "1"
            res = backtrack(i + 1, cur)
            if res:
                return res

        return backtrack(0, ["0" for c in nums])


if __name__ == '__main__':
    nums = ["00", "10"]
    s = Solution()
    a = s.findDifferentBinaryString(nums)
    print(a)
    nums = ["111", "011", "000"]
    a = s.findDifferentBinaryString(nums)
    print(a)
