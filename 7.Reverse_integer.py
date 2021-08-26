'''
Ссылка на описание задачи:
https://leetcode.com/problems/reverse-integer/
'''


class Solution(object):
    def reverse(self, x):
        if x < 0:
            x = int(str(x)[0] + str(x)[1:][::-1])
        else:
            x = int(str(x)[::-1])
        if x < -2**31 or x > 2**31 - 1:
            x = 0
        return x

