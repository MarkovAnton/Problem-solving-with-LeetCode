'''
Ссылка на описание задачи:
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
'''


class Solution(object):
    def searchRange(self, nums, target):
        result = []
        if target not in nums:
            return [-1, -1]

        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)

        result = [min(result), max(result)]
        return result

