'''
Ссылка на описание задачи:
https://leetcode.com/problems/valid-parentheses/
'''


class Solution(object):
    def isValid(self, s):
        brackets = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in s:
            if i in list(brackets.keys()):
                stack.append(i)
            elif stack and i == brackets[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []

