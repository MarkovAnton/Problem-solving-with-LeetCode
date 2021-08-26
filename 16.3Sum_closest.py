'''
Ссылка на описание задачи:
https://leetcode.com/problems/3sum-closest/
'''


class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        if len(nums) < 3 or len(nums) > 1000:
            return 0
        result = {}
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                summa = nums[i] + nums[j] + nums[k]
                result.update({abs(target - summa): summa})
                if summa > target:
                    k -= 1
                elif summa < target:
                    j += 1
                else:
                    return summa
        return result.get(min(result.keys()))

