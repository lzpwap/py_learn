'comment'

__author__ = 'lizhipei'

from typing import List
import math


# 冒泡排序
def get_short_nums(nums: List[int]) -> List[int]:
    num_len = len(nums)
    for index in range(num_len - 1):
        for mov in range(index, num_len):
            if nums[mov] < nums[index]:
                tmp = nums[mov]
                nums[mov] = nums[index]
                nums[index] = tmp
    return nums


# 归并排序
def merge_sort(nums: List[int]) -> List[int]:
    if len(nums) < 2:
        return nums
    middle = math.floor(len(nums) / 2)
    left = nums[0:middle]
    right = nums[middle:]
    return merge(merge_sort(left), merge_sort(right))


# 合并数组
def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


# 快速排序
def fast_sort(nums: List[int], start: int, end: int) -> List[int]:
    if start >= end:
        return
    left = start
    right = end
    anchor = nums[start]
    while left < right:
        while left < right and nums[right] >= anchor:
            right -= 1
        while left < right and nums[left] <= anchor:
            left += 1
        swap(nums, left, right)
    nums[start] = nums[left]
    nums[left] = anchor
    fast_sort(nums, start, right - 1)
    fast_sort(nums, right + 1, end)
    return nums


# 交换元素
def swap(nums: List[int], i: int, j: int):
    nums[i], nums[j] = nums[j], nums[i]
