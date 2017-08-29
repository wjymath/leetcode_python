# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        result = None
        r = result
        while head:
            if head.val == val:
                head = head.next
                continue
            tmp = head
            head = head.next
            if result == None:
                result = tmp
                result.next = None
                r = result
                continue
            result.next = tmp
            result = tmp
            result.next = None
            if head == None:
                result.next = None
        return r

if __name__ == '__main__':
    head = ListNode(1)
    a = ListNode(2)
    head.next = a
    b = ListNode(6)
    # a.next = b
    c = ListNode(3)
    b.next = c
    d = ListNode(4)
    c.next = d
    e = ListNode(5)
    d.next = e
    f = ListNode(6)
    e.next = f
    result = Solution().removeElements(head, 2)
    while result:
        print result.val
        result = result.next