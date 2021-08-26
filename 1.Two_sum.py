'''
Ссылка на описание задачи:
https://leetcode.com/problems/two-sum/
'''


class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target:
                    if i != j:
                        return [i, j]

