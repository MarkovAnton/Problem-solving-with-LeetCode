'''
Ссылка на описание задачи:
https://leetcode.com/problems/3sum/
'''


class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        if len(nums) <= 2:
            return []
        result = set()
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                summa = nums[i] + nums[j] + nums[k]
                if summa == 0:
                    result.add((nums[i], nums[j], nums[k]))
                    j, k = j + 1, k - 1
                elif summa > 0:
                    k -= 1
                else:
                    j += 1
        return list(result)

