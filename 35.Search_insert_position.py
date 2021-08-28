'''
Ссылка на описание задачи:
https://leetcode.com/problems/search-insert-position/
'''


class Solution(object):
    def searchInsert(self, nums, target):
        try:
            ind = nums.index(target)
        except:
            nums.append(target)
            nums.sort()
            ind = nums.index(target)

        return ind

