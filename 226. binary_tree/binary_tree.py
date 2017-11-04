# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        if root.right and root.left:
            tmp = root.right
            root.right = root.left
            root.left = tmp
            self.invertTree(root.left)
            self.invertTree(root.right)
        elif root.left:
            root.right = root.left
            root.left = None
            self.invertTree(root.right)
        elif root.right:
            root.left = root.right
            root.right = None
            self.invertTree(root.left)
        return root