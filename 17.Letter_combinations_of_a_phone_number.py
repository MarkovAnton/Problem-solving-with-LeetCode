'''
Ссылка на описание задачи:
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''


class Solution(object):
    def letterCombinations(self, digits):
        phone = {
            '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']
        }
        chars = []
        if len(digits) == 0:
            return []

        def backtrack(first=0, char=''):
            if len(char) == len(digits):
                chars.append(char)
                return
            for i in range(first, len(digits)):
                for elem in phone.get(digits[i]):
                    char += elem
                    backtrack(i + 1, char)
                    char = char[:-1]
        backtrack()
        return chars

