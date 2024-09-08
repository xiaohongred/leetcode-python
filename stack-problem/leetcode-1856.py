from typing import List


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        res = 0
        stack = []  # [(start, val), (start, val)]
        prefix = [0]

        for n in nums:
            prefix.append(prefix[-1] + n)  # prefis[i] 代表 nums [0, i) 之间所有元素的和

        for i, n in enumerate(nums):
            newStart = i
            while stack and stack[-1][1] > n:  # nums = [2, 1] , stack = [(0,2)], 当前正在处理元素1， 也就是 i=1, n = 1时，处理这种情况
                start, val = stack.pop()  # start = 0, val = 2
                total = prefix[i] - prefix[start]  # prefix[1] - prefix[0] = nums[0]
                res = max(res, val * total)
                newStart = start  # newStart = 0 因为 n < 之前的栈顶元素，所以可以认为n为最小值的连续子数组，可以包含之前的栈顶元素
            stack.append((newStart, n))  # stack = [(0, 1)]
        # stack = [(start, val), (start, val)] 中存的每个元素，
        #   代表nums中索引从 start 开始，值为val的元素，到nums 数组最后一个元素，val 都是最小值，
        #   因为如果stack 中的 val 不是最小值，在上面的 while stack and stack[-1][1] > n: 条件中就已经出栈了
        for start, val in stack:  # stack 中的元素是单调递增的，比如 1 2 2
            total = prefix[len(nums)] - prefix[start]
            # prefix[0] = 0,
            # prefix[1] = 0 + nums[0],
            # prefix[2] = nums[0] + nums[1]
            res = max(res, total * val)
        return res % (10 ** 9 + 7)

    def maxSumMinProduct_2(self, nums: List[int]) -> int:
        res = 0
        stack = []  # [(start, val), (start, val)]
        prefix = [0]

        for n in nums:
            prefix.append(prefix[-1] + n)  # prefis[i] 代表 nums [0, i) 之间所有元素的和

        for i, n in enumerate(nums):
            newStart = i
            while stack and stack[-1][1] > n:
                # nums = [1, 2, 3, 2] , stack = [(0,1),(1,2), (2,3)], 当前正在处理元素2， 也就是 i=3, n = 2时
                start, val = stack.pop()  # start = 2, val = 3
                total = prefix[i] - prefix[start]  # prefix[3] - prefix[2] = nums[2] = 3
                res = max(res, val * total)
                # newStart = 2 因为 n < 之前的栈顶元素(3)，
                # 所以可以认为n为最小值的连续子数组，可以包含之前的栈顶元素,
                # 这里的的影响是在下面遍历单调栈时会在total中包含 nums[start]   --> # prefix[4] - prefix[2] = nums[3] + nums[2]
                newStart = start
            stack.append((newStart, n))  # stack = [(0,1),(1,2),(2,2)]
        # stack 中的元素是单调递增的，比如 stack = [(0,1),(1,2),(2,2)]

        # stack = [(start, val), (start, val)] 中存的每个元素，
        #   代表nums中索引从 start 开始，值为val的元素，到nums 数组最后一个元素，val 都是最小值，
        #   因为如果stack 中的 val 不是最小值，在上面的 while stack and stack[-1][1] > n: 条件中就已经出栈了
        # len(nums) = 4
        for start, val in stack:
            total = prefix[len(nums)] - prefix[start]  # prefix[4] - prefix[2] = nums[3] + nums[2]
            res = max(res, total * val)
            # prefix[0] = 0,
            # prefix[1] = 0 + nums[0],
            # prefix[2] = nums[0] + nums[1],
            # prefix[3] = nums[0] +nums[1] + nums[2]
            # prefix[4] = nums[0] +nums[1] + nums[2] + nums[3]

        return res % (10 ** 9 + 7)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 2]
    a = s.maxSumMinProduct(nums)
    print(a)

    nums = [2, 3, 3, 1, 2]
    a = s.maxSumMinProduct(nums)
    print(a)

    nums = [3, 1, 5, 6, 4, 2]
    a = s.maxSumMinProduct(nums)
    print(a)

    nums = [1, 2, 3, 2]
    a = s.maxSumMinProduct_2(nums)
    print(a)

    nums = [2, 3, 3, 1, 2]
    a = s.maxSumMinProduct_2(nums)
    print(a)

    nums = [3, 1, 5, 6, 4, 2]
    a = s.maxSumMinProduct_2(nums)
    print(a)
