'''
Ссылка на описание задачи:
https://leetcode.com/problems/generate-parentheses/
'''


class Solution(object):
    def generateParenthesis(self, n):
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n - 1 - c):
                    ans.append('({}){}'.format(left, right))
        return ans

