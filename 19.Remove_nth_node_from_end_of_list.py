'''
Ссылка на описание задачи:
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        lst = []
        res = ans = ListNode()
        while head:
            lst.append(head.val)
            head = head.next
        del lst[-n]
        for i in lst:
            ans.next = ListNode(i)
            ans = ans.next
        return res.next

