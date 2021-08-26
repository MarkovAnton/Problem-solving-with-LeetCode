'''
Ссылка на описание задачи:
https://leetcode.com/problems/roman-to-integer/
'''


class Solution(object):
    def romanToInt(self, s):
        store = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        summa = 0
        for i in range(len(s)-1):
            if store.get(s[i]) < store.get(s[i+1]):
                summa -= store.get(s[i])
            else:
                summa += store.get(s[i])
        summa += store.get(s[len(s)-1])
        return summa

