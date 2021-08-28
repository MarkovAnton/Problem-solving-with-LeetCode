'''
Ссылка на описание задачи:
https://leetcode.com/problems/count-and-say/
'''


class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return '1'
        nums = self.countAndSay(n - 1)
        result = ''
        count = 0
        curr_num = nums[0]

        for i in range(len(nums)):
            if curr_num == nums[i]:
                count += 1
            else:
                result += str(count) + curr_num
                curr_num = nums[i]
                count = 1

        return result + str(count) + curr_num

