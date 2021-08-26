'''
Ссылка на описание задачи:
https://leetcode.com/problems/4sum/
'''


class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        N = len(nums)
        if N <= 3:
            return []
        result = set()
        for a in range(N - 3):
            for b in range(a + 1, N - 2):
                for c in range(b + 1, N - 1):
                    d = target - (nums[a] + nums[b] + nums[c])
                    if d in nums[c + 1:]:
                        result.add((nums[a], nums[b], nums[c], d))
        return list(result)

