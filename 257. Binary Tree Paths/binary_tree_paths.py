# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def format_data(self, input):
        result = ""
        for item in input:
            if result == "":
                result = str(item.val)
                continue
            result = result + "->" + str(item.val)
        return result.strip("->")
    def gen_str(self, input, result):
        tmp = input[-1]
        if not tmp.left and not tmp.right:
            result += [self.format_data(input)]
        if tmp.left:
            left_input = input + [tmp.left]
            self.gen_str(left_input, result)
        if tmp.right:
            right_input = input + [tmp.right]
            self.gen_str(right_input, result)
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        result = []
        self.gen_str([root], result)
        return result
