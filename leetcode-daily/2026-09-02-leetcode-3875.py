class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # 奇数
        canFlag1 = True
        for idx, n in enumerate(nums1):
            if n % 2 != 0:
                continue

            tempFlag = False
            for j, m in enumerate(nums1):
                if j == idx:
                    continue

                num2 = n - m
                if num2 % 2 != 0:
                    tempFlag = True
                    break
            if tempFlag:
                continue

            canFlag1 = False
            break
        if canFlag1:
            return True
        # 偶数
        canFlag2 = True
        for idx, n in enumerate(nums1):
            if n % 2 == 0:
                continue

            
            tempFlag = False
            for j, m in enumerate(nums1):
                if j == idx:
                    continue

                num2 = n - m
                if num2 % 2 == 0:
                    tempFlag = True
                    break

            if tempFlag:
                continue

            canFlag2 = False
            break
        return canFlag1 or canFlag2

if __name__ == "__main__":
    solution = Solution()
    nums1 = [2,3]
    result = solution.uniformArray(nums1)
    print(result)  # Output: True or False based on the implementation

    nums1 = [4,6]
    result = solution.uniformArray(nums1)
    print(result)  # Output: True or False based on the implementation