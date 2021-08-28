'''
Ссылка на описание задачи:
https://leetcode.com/problems/swap-nodes-in-pairs/
'''


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        lst = []
        res = ans = ListNode(0)
        while head:
            lst.append(head.val)
            head = head.next
        for i in range(1, len(lst)):
            if (i + 1) % 2 == 0:
                first = lst[i - 1]
                second = lst[i]
                lst[i] = first
                lst[i - 1] = second
        for i in lst:
            ans.next = ListNode(i)
            ans = ans.next
        return res.next

