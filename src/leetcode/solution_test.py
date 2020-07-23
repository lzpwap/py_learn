from solution import Solution
from solution import ListNode

solution = Solution()

# data = [-11, -3, -6, 12, -15, -13, -7, -3, 13, -2, -10, 3, 12, -12, 6, -6, 12, 9, -2, -12, 14, 11, -4, 11, -8, 8, 0,
#         -12, 4, -5, 10, 8, 7, 11, -3, 7, 5, -3, -11, 3, 11, -13, 14, 8, 12, 5, -12, 10, -8, -7, 5, -9, -11, -14, 9, -12,
#         1, -6, -8, -10, 4, 9, 6, -3, -3, -12, 11, 9, 1, 8, -10, -3, 2, -11, -10, -1, 1, -15, -6, 8, -7, 6, 6, -10, 7, 0,
#         -7, -7, 9, -8, -9, -9, -14, 12, -5, -10, -15, -9, -15, -7, 6, -10, 5, -7, -14, 3, 8, 2, 3, 9, -12, 4, 1, 9, 1,
# -15, -13, 9, -14, 11, 9]
# data = [-4,-1,-4,0,2,-2,-4,-3,2,-3,2,3,3,-4]
# data = [0, 3, 0, 1, 1, -1, -5, -5, 3, -3, -3, 0]
# data = [-1, 0, 1, 2, -1, -4]
# result = solution.threeSum(data)

# print(solution.threeSumClosest([-1,2,1,-4],1))

# print(solution.letterCombinations("234"))

# print(solution.maxCoins([3, 1, 5, 8]))

# print("isValid={}".format(solution.isValid("(]")))
# print("isValid={}".format(solution.isValid("()")))
# print("isValid={}".format(solution.isValid("")))
# print("isValid={}".format(solution.isValid("[(){}]")))
# print("isValid={}".format(solution.isValid("[(){}]()")))

head1 = ListNode()
list1 = head1
list1.val = 1
list1.next = ListNode()
list1 = list1.next
list1.val = 3
list1.next = ListNode()
list1 = list1.next
list1.val = 5

head2 = ListNode()
list2 = head2
list2.val = 2
list2.next = ListNode()
list2 = list2.next
list2.val = 4
list2.next = ListNode()
list2 = list2.next
list2.val = 6


result = solution.mergeTwoLists(head1,head2)
print(result)

result = solution.generateParenthesis(3)
print(result)
