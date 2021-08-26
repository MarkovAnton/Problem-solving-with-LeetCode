'''
Ссылка на описание задачи:
https://leetcode.com/problems/integer-to-roman/
'''


class Solution(object):
    def intToRoman(self, num):
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thous = ["", "M", "MM", "MMM", "MMMM"]
        thou = thous[num // 1000]
        hund = hunds[num // 100 % 10]
        ten = tens[num // 10 % 10]
        one = ones[num % 10]
        return thou + hund + ten + one

