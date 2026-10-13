class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers)-1

        while left < right:
            s = numbers[left] + numbers[right]

            if s == target:
                break
            if s > target:
                right -= 1
            else:
                left += 1
        
        return [left+1, right+1]


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))  # [1, 2]
    print(s.twoSum([2, 3, 4], 6))       # [1, 3]
    print(s.twoSum([-1, 0], -1))        # [1, 2]