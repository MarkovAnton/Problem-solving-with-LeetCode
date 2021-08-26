'''
Ссылка на описание задачи:
https://leetcode.com/problems/zigzag-conversion/
'''


class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        n = len(s)
        cycleLen = 2 * numRows - 2
        strList = []
        for i in range(numRows):
            for j in range(i, n, cycleLen):
                strList.append(s[j])
                if i != numRows - 1 and i != 0 and j + cycleLen - 2 * i < n:
                    strList.append(s[j + cycleLen - 2 * i])
        newstr = ''.join(strList)
        return newstr

