' solution '

__author__ = 'lizhipei'

from typing import List
from comment import fast_sort
import math

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# 搜索树节点
class TreeNode:
    def __init__(self, left:int,right:int,count:int,res:str):
        self.left:int = left
        self.right:int = right
        self.count:int = count
        self.res:str = res

class Solution:

    # 数字 n 代表生成括号的对数，
    # 请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
    # 分治法，每次进入函数继续生成新括号（，也可能闭合括号），最后括号用完后，添加结果集
    #   我的思路是，先往字符串中添加一个左括号
    #   然后进入函数时，根据当前节点剩余的左括号和右括号分两个分支继续探索，
    #   用一个变量限制右括号和左括号的平衡，层层探索。
    #   直到探索完所有的路径，最后添加到结果集，
        # 深度优先遍历（深度探索出某个路径再回溯到起点后再继续探索另一条路径）
    def generateParenthesis(self, n: int) -> List[str]:
        result:List[str] = []
        self.computeResult(result,"(",n-1,n,1)
        return result
    
    def computeResult(self,result,start:str,startN:int,endN:int,count:int):
        if count>=0 and startN>0:
            self.computeResult(result,start+"(",startN-1,endN,count+1)
        if count>0 and endN>0:
            self.computeResult(result,start+")",startN,endN-1,count-1)
        if count==0 and startN==0 and endN==0:
            result.append(start)
    

    
    # 广度优先遍历
    def generateParenthesis_2(self, n: int) -> List[str]:
        result:List[str] = []
        nodeList:List[TreeNode] = [TreeNode(n,n,0,"")]
        while nodeList:
            # 通过一个数组（栈/队列）的pop的位置来决定是深度优先，还是广度优先。
            # 如果是先进先出那就是广度优先，先进后出就是深度优先，
            current = nodeList.pop()
            if current.left>0 and current.count>=0:
                newNode = TreeNode(current.left-1,current.right,current.count+1,current.res+"(")
                nodeList.append(newNode)
            if current.right>0 and current.count>0:
                newNode = TreeNode(current.left,current.right-1,current.count-1,current.res+")")
                nodeList.append(newNode)
            if current.right==0 and current.left==0 and current.count==0:
                result.append(current.res)
        return result


    # 动态规划
    def generateParenthesis_1(self, n: int) -> List[str]:
        pass



    # 将两个升序链表合并为一个新的 升序 链表并返回。
    # 新链表是通过拼接给定的两个链表的所有节点组成的。
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result:ListNode = None
        head = result
        list1 = l1
        list2 = l2
        if list1 and list2:
            if list1.val<list2.val:
                result = list1
                head = result
                list1 = list1.next
            else:
                result = list2
                head = result
                list2 = list2.next  
        elif list1:
            result = list1
            head = result
            list1 = list1.next
        elif list2:
            result = list2
            head = result
            list2 = list2.next  
        
        while list1 and list2:
            if list1.val < list2.val:
                result.next = list1
                result = result.next
                list1 = list1.next
            else:
                result.next = list2
                result = result.next
                list2 = list2.next
        while list1:
            result.next = list1
            result = result.next
            list1 = list1.next
        while list2:
            result.next = list2
            result = result.next
            list2 = list2.next
        return head

    #   给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
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
