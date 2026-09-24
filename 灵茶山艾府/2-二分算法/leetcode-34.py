from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        题意：在升序数组 nums 中找出 target 出现的**第一个**和**最后一个**位置，
        不存在则返回 [-1, -1]。要求时间复杂度 O(log n)。

        思路：做两次二分，分别求出「下界」和「上界」。
        - find_left  ：第一个满足 nums[i] >= target 的下标（相当于 bisect_left），
                       若 target 存在，它就是 target 的起始位置。
        - find_right ：最后一个满足 nums[i] <= target 的下标（相当于 bisect_right - 1），
                       若 target 存在，它就是 target 的结束位置。

        二分的关键在于「>= 时把右边界往左压」还是「<= 时把左边界往右压」，
        并且最后要返回的到底是 left 还是 right —— 见下面两个函数里的说明。
        """

        def find_left() -> int:
            """返回第一个 >= target 的下标（下界 / 左闭区间起点）。"""
            left, right = 0, len(nums) - 1   # 在闭区间 [left, right] 里查找
            while left <= right:             # 区间为空时退出（此时 left == right + 1）
                mid = (left + right) // 2

                # nums[mid] >= target：mid 可能就是答案，也可能太靠右，
                # 所以把 mid 保留在「候选区间的左侧」外，令 right = mid - 1。
                # 因为就算 mid 正好等于 target，左边还可能有相同的值。
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    # nums[mid] < target：mid 及其左边都太小，答案一定在右边
                    left = mid + 1

            # 循环结束时 left == right + 1，left 就是第一个 >= target 的位置
            # （也可能等于 len(nums)，表示所有元素都小于 target）
            return left

        def find_right() -> int:
            """返回最后一个 <= target 的下标（上界，等价于 bisect_right - 1）。"""
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2

                # nums[mid] <= target：mid 可能就是答案，也可能太靠左，
                # 因为右边还可能有相同的值，所以继续往右找。
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    # nums[mid] > target：mid 及其右边都太大，答案一定在左边
                    right = mid - 1

            # 循环结束时 right == left - 1，right 就是最后一个 <= target 的位置
            # （也可能等于 -1，表示所有元素都大于 target）
            return right

        left_idx = find_left()    # target 的左端点候选
        right_idx = find_right()  # target 的右端点候选

        # 求出两个边界后还要验证 target 真的存在，因为下界不一定是 target 本身。
        # 判空：left_idx == len(nums) 表示数组里没有 >= target 的元素；
        # 判存在：nums[left_idx] 必须正好等于 target。
        # （若 nums[left_idx] == target 成立，则 left_idx <= right_idx 必然成立，
        #   这半句属于防御性写法，可省略。）
        if left_idx <= right_idx and left_idx < len(nums) and nums[left_idx] == target:
            return [left_idx, right_idx]

        return [-1, -1]


    def searchRangeV2(self, nums: List[int], target: int) -> List[int]:
        """
        写法二：只写一个二分（lower_bound），通过「换个查询值」把上界也算出来。

        用到的数学关系：
            最后一个 <= target 的位置  =  (第一个 >= target + 1 的位置) - 1

        直觉：把 target 换成 target + 1 再求下界，得到的是「target 连续区间」右边界的
        下一个位置，所以减 1 就落在 target 的最后一个位置上。
        这样就不用再写一个方向相反的二分了，逻辑复用、也更不容易写错。
        """

        def lower_bound(nums: List[int], target: int) -> int:
            """
            返回第一个 >= target 的下标（下界）。
            若数组里所有元素都 < target，则返回 len(nums)（注意这个返回值会越界，
            所以调用方拿到结果后必须自己判越界）。
            """
            left, right = 0, len(nums) - 1   # 在闭区间 [left, right] 中查找
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    # mid 可能就是答案（等于 target），但左边还可能有相同的值，
                    # 所以继续往左找更靠前的那个
                    right = mid - 1
                else:
                    # nums[mid] < target：mid 及其左边都不可能是答案
                    left = mid + 1
            # 循环退出时 left == right + 1，left 就是第一个 >= target 的位置
            return left

        # 第一步：求 target 的左端点
        start = lower_bound(nums, target)

        # 下界可能越界（所有元素 < target），也可能落在别的值上（target 不存在）
        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        # 第二步：求 target 的右端点，复用同一个 lower_bound
        # lower_bound(nums, target + 1) 是「第一个 > target」的位置（即 target + 1 的下界），
        # 也就是 target 区间右边界再往右一格，因此减 1 才是最后一个 target 的下标。
        end = lower_bound(nums, target + 1) - 1

        return [start, end]


if __name__ == "__main__":
    solution = Solution()

    # 每个用例同时跑两种写法，输出必须一致
    cases = [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),    # 目标出现两次
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),  # 目标不存在（下界指向 7）
        ([], 0, [-1, -1]),                   # 空数组，下界 = 0 = len(nums)
        ([1], 1, [0, 0]),                    # 只有一个元素，且正好是目标
        ([1, 2, 3], 3, [2, 2]),              # 目标在末尾，target + 1 的下界越界（= len）
        ([1], 0, [-1, -1]),                  # 目标比所有元素都小
    ]

    for nums, target, expected in cases:
        r1 = solution.searchRange(nums, target)
        r2 = solution.searchRangeV2(nums, target)
        print(f"nums={nums}, target={target} -> V1={r1}, V2={r2}, 期望={expected}")