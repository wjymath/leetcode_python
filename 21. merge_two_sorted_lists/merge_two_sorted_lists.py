# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def list_sort(self, l1, l2):
        if l1.val > l2.val:
            result = l2.val
            l2 = l2.next
        else:
            result = l1.val
            l1 = l1.next
        return [result, l1, l2]

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0) #init list with value 0 and return head next list
        head = result
        while l1 and l2:
            tmp = ListNode(None)
            [tmp.val, l1, l2] = self.list_sort(l1, l2)
            result.next = tmp
            result = tmp
        if l1:
            result.next = l1
        else:
            result.next = l2
        return head.next
if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(2)
    print Solution().mergeTwoLists(l1, l2).val
    print Solution().mergeTwoLists(l1,l2).next.val