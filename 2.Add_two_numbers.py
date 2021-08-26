'''
Ссылка на описание задачи:
https://leetcode.com/problems/add-two-numbers/
'''


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2, c=0):
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10)
        if (l1.next is not None or l2.next is not None or c != 0):
            if l1.next is None:
                l1.next = ListNode(0)
            if l2.next is None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next, l2.next, c)
        return ret

