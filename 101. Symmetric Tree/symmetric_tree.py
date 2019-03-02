# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isexit(self, left_child, right_child):
        if not left_child and not right_child:
            return True
        if not left_child or not right_child:
            return False

        if left_child.val != right_child.val:
            return False

        if left_child.val == right_child.val:
            return self.isexit(left_child.left, right_child.right) and self.isexit(left_child.right, right_child.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isexit(root, root)