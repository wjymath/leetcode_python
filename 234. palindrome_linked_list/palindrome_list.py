class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        result = []
        if head == None:
            return True
        while head:
            result += [head.val]
            head = head.next
        return result == result[::-1]