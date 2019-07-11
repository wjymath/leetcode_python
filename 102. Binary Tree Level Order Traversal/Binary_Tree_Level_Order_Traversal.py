# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ava_list = [root]
        result = []
        while ava_list:
            new_ava_list = []
            tmp_result = []
            for item in ava_list:
                tmp_result.append(item.val)
                if item.left:
                    new_ava_list.append(item.left)
                if item.right:
                    new_ava_list.append(item.right)
            result.append(tmp_result)
            ava_list = new_ava_list
        return result