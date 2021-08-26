'''
Ссылка на описание задачи:
https://leetcode.com/problems/string-to-integer-atoi/
'''


class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        num = ''
        if len(s) == 0:
            return 0
        if s[0] not in ('0', '1', '2', '3', '4', '5',
                        '6', '7', '8', '9', '+', '-'):
            return 0
        else:
            if s[0] in ['+', '-']:
                num += s[0]
                s = s[1:]
            for i in range(len(s)):
                if s[i].isdigit():
                    num += s[i]
                elif s[i].isalpha() or s[i] in ['.', '+', '-', ' ']:
                    break
            if num in ['+', '-', '']:
                return 0
            else:
                num = int(num)
                if -2**31 <= num <= 2**31 - 1:
                    return num
                elif num < -2**31:
                    return -2**31

                else:
                    return 2**31 - 1

