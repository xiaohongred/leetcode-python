class Solution:
    def isHappy(self, n: int) -> bool:
        mySet = set()
        while True:
            mySum = self.sumOfSquares(n)

            if mySum == 1:
                return True

            if mySum in mySet:
                return False
            else:
                mySet.add(mySum)
            n = mySum
    def sumOfSquares(self, nums: int) -> int:
        mySum = 0
        while nums:
            digit = nums % 10
            nums = nums // 10
            mySum += digit*digit

        return mySum


if __name__ == '__main__':
    s = Solution()
    a = s.isHappy(19)
    print(a)