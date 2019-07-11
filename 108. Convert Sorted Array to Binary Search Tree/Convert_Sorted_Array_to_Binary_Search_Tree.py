# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
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

if __name__ == "__main__":
    print(Solution().sortedArrayToBST([-10,-3,0,5,9]))
