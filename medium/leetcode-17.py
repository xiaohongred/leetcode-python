from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitsMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "gprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i: int, curStr: str):
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            for c in digitsMap[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")
        return res


if __name__ == '__main__':
    digits = "23"
    s = Solution()
    a = s.letterCombinations(digits)
    print(a)
