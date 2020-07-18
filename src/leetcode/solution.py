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


class Solution:
    # 两数之和，双指针
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = fast_sort(nums, 0, len(nums)-1)
        # nums.sort()
        print(nums)
        result = []
        for index in range(len(nums)):
            left = index + 1
            right = len(nums) - 1
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            curr_num = -nums[index]
            while left < right:
                if nums[left] + nums[right] < curr_num:
                    left += 1
                elif nums[left] + nums[right] > curr_num:
                    right -= 1
                elif nums[left] + nums[right] == curr_num:
                    result.append([nums[index], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result

    # 暴力解法
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        x = 0
        y = 0
        z = 0
        result = []
        for numx in nums:
            y = 0
            for numy in nums:
                z = 0
                for numz in nums:
                    if x != y and y != z and x != z:
                        if numx + numy + numz == 0:
                            shortNum = get_short_nums([numx, numy, numz])
                            isResultItem = not self.find_list(result, shortNum)
                            if isResultItem:
                                result.insert(len(result) + 1, shortNum)
                    z = z + 1
                y = y + 1
            x = x + 1
        return result

    def find_list(self, result: List[List[int]], nums: List[int]) -> bool:
        for numList in result:
            index = 0
            all_fill = True
            for num in numList:
                if nums[index] != num:
                    all_fill = False
                    break
                index += 1
            if all_fill:
                return True
        return False
