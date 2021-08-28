'''
Ссылка на описание задачи:
https://leetcode.com/problems/longest-valid-parentheses/
'''


class Solution(object):
    def longestValidParentheses(self, s):
        stack = []
        best = 0
        for i in s:
            if i == '(':
                stack.append(i)
            elif stack and stack[-1] == '(':
                stack.pop()
                stack.append(2)
                best = max(best, stack[-1])
            elif len(stack) >= 2
            and isinstance(stack[-1], int)
            and stack[-2] == '(':
                stack[-2] = stack[-1] + 2
                stack.pop()
                best = max(best, stack[-1])
            else:
                stack = []

            while len(stack) >= 2
            and isinstance(stack[-1], int)
            and isinstance(stack[-2], int):
                temp = stack.pop()
                stack[-1] += temp
                best = max(best, stack[-1])

        return best

