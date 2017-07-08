# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(l1.val)
        head = result
        while l1 and l2:
            tmp  = ListNode(None)
            tmp.val = l1.val + l2.val
            result.next = tmp
            result = tmp
            l1 = l1.next
            l2 = l2.next
        if l1:
            result.next = l1
        else:
            result.next = l2
        count = 0
        result = head.next
        while result:
            result.val += count
            count = result.val / 10
            result.val %= 10
            tmp = result
            result = result.next
        if count:
            tmp.next = ListNode(count)
        return head.next