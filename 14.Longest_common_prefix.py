'''
Ссылка на описание задачи:
https://leetcode.com/problems/longest-common-prefix/
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:len(prefix)-1]
                if prefix == '':
                    return ''
        return prefix

