'''
Ссылка на описание задачи:
https://leetcode.com/problems/palindrome-number/
'''


class Solution(object):
    def isPalindrome(self, x):
        if str(x)[::-1] == str(x):
            return True
        else:
            return False

