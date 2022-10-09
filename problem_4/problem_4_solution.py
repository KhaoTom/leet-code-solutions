def find_median_sorted_arrays(nums1, nums2):
    nums = sorted(nums1 + nums2)
    len_nums = len(nums)
    if len_nums == 0:
        return 0
    if len_nums == 1:
        return nums[0]
    middle = len_nums // 2
    if len_nums % 2 == 0:
        return (nums[middle - 1] + nums[middle]) / 2
    return nums[middle]
