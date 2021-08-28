'''
Ссылка на описание задачи:
https://leetcode.com/problems/combination-sum-ii/
'''


from itertools import combinations


class Solution(object):
    def combinationSum2(self, candidates, target):
        result = []

        for n in range(1, 1 + len(candidates)):
            for item in combinations(candidates, n):
                if (not sorted(item) in result) and (sum(item) == target):
                    result.append(sorted(item))

        return result

