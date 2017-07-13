# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tree_dep(self, root):
        if not root:
            return 0
        while root.left or root.right:
            return 1 + max(self.tree_dep(root.left), self.tree_dep(root.right), 0)
        return 0
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.left and root.right:
            if abs(self.tree_dep(root.left) - self.tree_dep(root.right)) > 1:
                return False
            return self.isBalanced(root.left) & self.isBalanced(root.right)
        if self.tree_dep(root) > 1:
            return False
        return True

if __name__ == '__main__':
    a = TreeNode(5)
    b = TreeNode(4)
    c = TreeNode(11)
    d = TreeNode(7)
    e = TreeNode(2)
    f = TreeNode(8)
    g = TreeNode(13)
    h = TreeNode(4)
    i = TreeNode(1)
    a.right = b
    b.right = c
    # a.left = b
    # b.left = c
    # c.left = d
    # c.right = e
    # a.right = f
    # f.left = g
    # f.right = h
    # h.right = i
    # aa = TreeNode([1])
    print Solution().isBalanced(a)