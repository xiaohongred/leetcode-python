def insertion_sort(arr):
    # 从第二个元素开始
    for i in range(1, len(arr)):
        key = arr[i]  # 当前准备插入的元素

        # 从当前元素的前一个位置开始往前找
        j = i - 1

        # 如果前面的元素比 key 大，就向后移动
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # 找到合适的位置，插入 key
        arr[j + 1] = key

    return arr


nums = [5, 2, 4, 6, 1, 3]

print(insertion_sort(nums))
