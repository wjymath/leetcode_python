# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        walk = head
        faster = walk.next
        while walk and faster:
            if walk == faster:
                return True
            if not faster.next or not faster.next.next or not walk.next:
                return False
            faster = faster.next.next
            walk = walk.next
        return False