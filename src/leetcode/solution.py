'solution'

__author__ = 'lizhipei'

from typing import List
from comment import fast_sort
import math


class Solution:

    #    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
    #   有效字符串需满足：
    #   左括号必须用相同类型的右括号闭合。
    #   左括号必须以正确的顺序闭合。
    #   注意空字符串可被认为是有效字符串。
    def isValid(self, s: str) -> bool:
        help_list = []
        if len(s)%2 !=0:
            return False
        for char in s:
            if not help_list:
                help_list.append(char)
            else:
                c = help_list.pop()
                if c == '{':
                    if char == '}':
                        continue
                elif c == '(':
                    if char == ')':
                        continue
                elif c == '[':
                    if char == ']':
                        continue
                help_list.append(c)
                help_list.append(char)
        if help_list:
            return False
        else:
            return True

    # 戳气球
    def maxCoins(self, nums: List[int]) -> int:
        result = 0
        return result

    #  电话号码的字母组合
    #  动态规划，每个字符的结果集依赖于先前一个字符的结果集
    def letterCombinations(self, digits: str) -> List[str]:
        map = {'2': "abc",
               '3': "def",
               '4': "ghi",
               '5': "jkl",
               '6': "mno",
               '7': "pqrs",
               '8': "tuv",
               '9': "wxyz",
               }
        result = []
        for c in digits:
            if c in map:
                c_map = map[c]
                if result:
                    result = [x + y for x in result for y in c_map]
                else:
                    result = [i for i in c_map]
        return result

    # 最接近三数之和
    # 数组遍历+双指针，逼近结果
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for index in range(len(nums)):
            left = index + 1
            right = len(nums) - 1
            while left < right:
                tmp = nums[index] + nums[left] + nums[right]
                if tmp == target:
                    return tmp
                elif abs(tmp - target) < abs(result - target):
                    result = tmp
                if tmp < target:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return result

    # 两数之和，双指针
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = fast_sort(nums, 0, len(nums) - 1)
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
