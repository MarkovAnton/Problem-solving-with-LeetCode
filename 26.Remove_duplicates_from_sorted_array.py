'''
Ссылка на описание задачи:
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''


class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

