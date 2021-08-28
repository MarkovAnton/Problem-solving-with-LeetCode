'''
Ссылка на описание задачи:
https://leetcode.com/problems/reverse-nodes-in-k-group/
'''


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        count = 0
        cur = head
        while (cur and count < k):
            cur = cur.next
            count += 1
        if count == k:
            rest = self.reverseKGroup(cur, k)
            prev = rest
            cur = head
            while count > 0:
                count -= 1
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            return prev
        return head

