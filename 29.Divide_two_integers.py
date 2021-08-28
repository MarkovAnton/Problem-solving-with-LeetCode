'''
Ссылка на описание задачи:
https://leetcode.com/problems/divide-two-integers/
'''


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            result = floor(dividend / divisor)
        else:
            result = ceil(dividend / divisor)

        if result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif result < -2 ** 31:
            return -2 ** 31

        return result

