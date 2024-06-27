from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        phontTable = {"2": "abc",
                      "3": "def",
                      "4": "ghi",
                      "5": "jkl",
                      "6": "mno",
                      "7": "pqrs",
                      "8": "tuv",
                      "9": "wxyz"}
        res = []
        path = ""

        def dfs(i):
            nonlocal path
            if i == len(digits):
                res.append(path)
                return
            for c in phontTable[digits[i]]:
                path = path + c
                dfs(i + 1)
                path = path[0: -1]

        dfs(0)
        return res

    def letterCombinationsV2(self, digits: str) -> List[str]:

        phontTable = {"2": "abc",
                      "3": "def",
                      "4": "ghi",
                      "5": "jkl",
                      "6": "mno",
                      "7": "pqrs",
                      "8": "tuv",
                      "9": "wxyz"}
        res = []

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in phontTable[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")
        return res


if __name__ == '__main__':
    digits = "23"
    s = Solution()
    a = s.letterCombinations(digits)
    print(a)

    a = s.letterCombinationsV2(digits)
    print(a)
