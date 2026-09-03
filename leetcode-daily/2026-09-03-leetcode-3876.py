class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums1.sort() # 排序数组
        # 奇数
        oddFlag = True
        for idx, n in enumerate(nums1):
            if n % 2 != 0:
                continue

            tempFlag = False
            for j, m in enumerate(nums1):
                if j == idx:
                    continue

                num2 = n - m
                if num2 < 1:
                    break
                if num2 >= 1 and num2 % 2 != 0:
                    tempFlag = True
                    break
            if tempFlag:
                continue

            oddFlag = False
            break
        if oddFlag:
            return True
        # 偶数
        evenFlag = True
        for idx, n in enumerate(nums1):
            if n % 2 == 0:
                continue

            
            tempFlag = False
            for j, m in enumerate(nums1):
                if j == idx:
                    continue

                num2 = n - m
                if num2 < 1:
                    break
                if num2 >= 1 and num2 % 2 == 0:
                    tempFlag = True
                    break

            if tempFlag:
                continue

            evenFlag = False
            break
        return oddFlag or evenFlag

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,4,7]
    result = solution.uniformArray(nums1)
    print(result)  # Output: True or False based on the implementation

    nums1 = [2,3]
    result = solution.uniformArray(nums1)
    print(result)  # Output: True or False based on the implementation


    nums1 = [4,6]
    result = solution.uniformArray(nums1)
    print(result)  # Output: True or False based on the implementation