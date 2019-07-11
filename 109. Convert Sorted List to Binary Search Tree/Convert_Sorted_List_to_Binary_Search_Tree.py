# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def convertList(self, head):
        tmp = head
        result = []
        while tmp:
            result.append(tmp.val)
            tmp = tmp.next
        return result

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        input_l = len(nums)
        if input_l == 0:
            return None
        t = TreeNode(nums[len(nums) // 2])
        t.left = self.sortedArrayToBST(nums[:input_l // 2])
        t.right = self.sortedArrayToBST(nums[input_l // 2 + 1:])
        return t

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        nums = self.convertList(head)

        input_l = len(nums)
        if input_l == 0:
            return None
        t = TreeNode(nums[len(nums) // 2])
        t.left = self.sortedArrayToBST(nums[:input_l // 2])
        t.right = self.sortedArrayToBST(nums[input_l // 2 + 1:])
        return t