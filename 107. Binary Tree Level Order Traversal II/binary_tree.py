# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        node = [root]
        while node != []:
            tmp = []
            layer = []
            for item in node:
                if item.left:
                    layer += [item.left]
                if item.right:
                    layer += [item.right]
                tmp += [item.val]
            result = [tmp] + result
            node = layer
        return result