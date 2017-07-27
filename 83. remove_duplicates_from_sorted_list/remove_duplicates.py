# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = head
        while head:
            if head.next:
                if head.val == head.next.val:
                    head.next = head.next.next
                else:
                    head = head.next
            else:
                head = None
        return result

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(1)
    c = ListNode(1)
    a.next = b
    b.next = c
    print Solution().deleteDuplicates(a).val
    print a.next.val
    print bool(a and a.next)
    print bool(a.next and a.next.next)