'''
Ссылка на описание задачи:
https://leetcode.com/problems/longest-palindromic-substring/
'''


class Solution(object):
    def longestPalindrome(self, s):
        for i in range(len(s), 0, -1):
            for j in range(len(s) - i + 1):
                palindrom = s[j:i+j]
                if palindrom == palindrom[::-1]:
                    return palindrom

