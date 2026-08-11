def partition(nums: list[int], left: int, right: int) -> int:
    """哨兵划分"""
    # 以 nums[left] 为基准数
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= nums[left]:
            j -= 1  # 从右向左找首个小于基准数的元素
        while i < j and nums[i] <= nums[left]:
            i += 1  # 从左向右找首个大于基准数的元素
        # 元素交换
        nums[i], nums[j] = nums[j], nums[i]
    # 将基准数交换至两子数组的分界线
    nums[i], nums[left] = nums[left], nums[i]
    return i  # 返回基准数的索引


def quick_sort(nums: list[int], left: int, right: int):
    """快速排序"""
    # 子数组长度为 1 时终止递归
    if left >= right:
        return
    # 哨兵划分
    pivot = partition(nums, left, right)
    # 递归左子数组、右子数组
    quick_sort(nums, left, pivot - 1)
    quick_sort(nums, pivot + 1, right)


nums = [5, 2, 4, 6, 1, 3]
quick_sort(nums, 0, len(nums) - 1)
print(nums)
