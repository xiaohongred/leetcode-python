from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charSet = set()

        def overlap(charSet, s):
            # c = Counter(charSet) + Counter(s)
            # return max(c.values()) > 1
            prev = set()
            for c in s:
                if c in charSet or c in prev:
                    return True
                prev.add(c)
            return False

        def backtrack(i):
            if i == len(arr):
                return len(charSet)
            res = 0
            if not overlap(charSet, arr[i]):  # 需要不重叠，才能加入charset
                for c in arr[i]:  # add arr[i] to charSet
                    charSet.add(c)
                res = backtrack(i + 1)  # 在包含 arr[i] 的情况下，结果字符串的长度
                for c in arr[i]:  # remove arr[i] from charSet
                    charSet.remove(c)

            resNotInclude = backtrack(i + 1)  # 在不包含 arr[i] 的情况下，结果字符串的长度
            return max(res, resNotInclude)

        return backtrack(0)


if __name__ == '__main__':
    arr = ["un", "iq", "ue"]
    s = Solution()
    a = s.maxLength(arr)
    print(a)
