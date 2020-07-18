from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = self.get_short_nums(nums)
        result = []
        for index in range(len(nums)):
            left = index + 1
            right = len(nums) - 1
            if index>0 and nums[index] == nums[index-1]:
                continue
            curr_num = -nums[index]
            while left < right:
                if nums[left] + nums[right] < curr_num:
                    left += 1
                elif nums[left] + nums[right] > curr_num:
                    right -= 1
                elif nums[left] + nums[right] == curr_num:
                    result.insert(len(result), [nums[index], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result

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
                            shortNum = self.get_short_nums([numx, numy, numz])
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

    def get_short_nums(self, nums: List[int]) -> List[int]:
        num_len = len(nums)
        for index in range(num_len - 1):
            for mov in range(index, num_len):
                if nums[mov] < nums[index]:
                    tmp = nums[mov]
                    nums[mov] = nums[index]
                    nums[index] = tmp
        return nums
