from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        题意：找出任意一个「峰值元素」的下标。峰值指严格大于左右相邻元素的元素。
        约定 nums[-1] = nums[n] = -∞，因此数组里一定存在峰值（哪怕长度为 1）。
        要求时间复杂度 O(log n)。

        核心思路：二分不是靠「有序」，而是靠「爬坡方向」。
        任取中点 mid，比较 nums[mid] 与 nums[mid + 1]：
        - 若 nums[mid] < nums[mid + 1]：说明 mid 处是上坡，右侧一定有峰值
          （一直往右爬，要么在某个点下降形成峰值，要么爬到最右端，
           而右端外面是 -∞，所以最右端就是峰值）-> 抛弃左半边，left = mid + 1
        - 若 nums[mid] > nums[mid + 1]：说明 mid 处是下坡，mid 自身或它左侧一定有峰值
          （往左爬同理，最左端外面是 -∞）-> 抛弃右半边，但 mid 仍可能是答案，right = mid

        注意：题目保证相邻元素不相等，所以不存在 nums[mid] == nums[mid + 1] 的情况。

        时间复杂度 O(log n)，空间复杂度 O(1)。
        """
        left, right = 0, len(nums) - 1  # 答案一定落在闭区间 [left, right] 内

        # 用 < 而不是 <=：区间只剩一个元素时它必然是峰值，不必再判断，
        # 循环结束时 left == right，直接返回即可。
        while left < right:
            mid = (left + right) // 2  # 下取整

            # 安全性：因为 left < right，所以 mid < right，即 mid + 1 <= right <= len-1，
            # 访问 nums[mid + 1] 永远不会越界。

            if nums[mid] < nums[mid + 1]:
                # 上坡：峰值在 mid 右侧，mid 自己肯定不是峰值，直接跳过
                left = mid + 1
            else:
                # 下坡（nums[mid] > nums[mid + 1]）：峰值在 mid 左侧或就是 mid 本身，
                # mid 不能丢，所以 right = mid（不是 mid - 1）
                right = mid

        return left  # 此时 left == right，就是峰值下标

    def findPeakElementV2(self, nums: List[int]) -> int:
        """
        写法二：左开右闭区间 + 哨兵（灵茶山艾府「红蓝染色法」的风格）。

        和写法一的区别只在「不变量的表达方式」：
            写法一：答案在**闭区间** [left, right] 内，left 和 right 都可能是答案。
            写法二：答案在**左开右闭区间** (left, right] 内，
                    也就是 left 永远是一个「确定不是答案」的边界哨兵，答案满足 index >= left + 1。

        初始 left = -1 是虚拟下标，可以理解成 nums[-1] = -∞ 的那个位置：
        它本来就不可能是答案（没有元素），拿它当左哨兵刚刚好。
        right = len(nums) - 1 是最后一个真实下标，一开始把整个数组都当作候选。

        这样写的好处：两个分支都只写 `= mid`，不用再纠结该写 mid 还是 mid ± 1。
        因为 mid 被划到哪一边，是由「它是否可能是答案」决定的，与下标加减无关。
        """
        left = -1                # 哨兵：确定不是答案的左侧边界
        right = len(nums) - 1    # 候选区间右端点（闭），答案落在 (left, right] 内

        # 区间内还有至少 2 个候选就继续二分。
        # 结束时 left + 1 == right，候选只剩 right 一个，它就是答案。
        while left + 1 < right:
            mid = (left + right) // 2   # left < mid < right，mid 必在候选区间内部

            # 安全性：mid < right <= len-1，所以 mid + 1 <= len-1，不会越界。

            if nums[mid] < nums[mid + 1]:
                # 上坡：答案严格在 mid 右侧，mid 及它左边全部排除，
                # 于是把「确定不是答案」的左哨兵推进到 mid
                left = mid
            else:
                # 下坡：答案在 mid 或它左侧，mid 依然可能是答案，
                # 所以右端点收缩到 mid（把 mid 留在候选区间里）
                right = mid

        return right    # left + 1 == right，候选唯一，即峰值下标


if __name__ == "__main__":
    solution = Solution()

    cases = [
        [1, 2, 3, 1],            # 峰值 3（索引 2）
        [1, 2, 1, 3, 5, 6, 4],   # 峰值 2（索引 1）或 6（索引 5）
        [1],                     # 单元素，本身就是峰值
        [1, 2],                  # 单调递增，右端点是峰值（nums[len] = -∞）
        [2, 1],                  # 单调递减，左端点是峰值（nums[-1] = -∞）
        [3, 1, 2],               # 两个端点都是峰值
    ]

    def is_peak(nums: List[int], i: int) -> bool:
        """校验下标 i 是否满足峰值定义（数组外侧视为 -∞）。"""
        left_ok = (i == 0) or nums[i] > nums[i - 1]
        right_ok = (i == len(nums) - 1) or nums[i] > nums[i + 1]
        return left_ok and right_ok

    # 两种写法都应该返回某个合法峰值（不一定相同，题目只要求任意一个）
    for nums in cases:
        i1 = solution.findPeakElement(nums)
        i2 = solution.findPeakElementV2(nums)
        print(f"nums={nums} -> V1={i1}(峰值?{is_peak(nums, i1)}), "
              f"V2={i2}(峰值?{is_peak(nums, i2)})")