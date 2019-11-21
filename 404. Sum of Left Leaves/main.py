# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution(object):
#     def sumOfLeftLeaves(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if not root:
#             return 0
#         if root.left and not root.left.left and not root.left.right:
#             return root.left.val + self.sumOfLeftLeaves(root.right)
#         return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        BFS = [[root]]
        result = 0
        while True:
            tmp_result = []
            for item in BFS[-1]:
                if item.left and not item.left.left and not item.left.right:
                    result += item.left.val
                if item.left and (item.left.left or item.left.right):
                    tmp_result.append(item.left)
                if item.right and (item.right.left or item.right.right):
                    tmp_result.append(item.right)
            if not tmp_result:
                break
            BFS.append(tmp_result)
        return result