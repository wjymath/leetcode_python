# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        rl = root.left
        rr = root.right
        if root.val == sum and rl == None and rr == None:
            return True
        if rl and rr:
            return self.hasPathSum(rl, sum - root.val) | self.hasPathSum(rr, sum - root.val)
        if rl:
            return self.hasPathSum(rl, sum - root.val)
        if rr:
            return self.hasPathSum(rr, sum - root.val)
        return False

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
    a.left = b
    b.left = c
    c.left = d
    c.right = e
    a.right = f
    f.left = g
    f.right = h
    h.right = i
    print Solution().hasPathSum([], 100)