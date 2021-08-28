'''
Ссылка на описание задачи:
https://leetcode.com/problems/combination-sum/
'''


class Solution(object):
    def combinationSum(self, candidates, target):
        ways = {index: [] for index in range(0, target + 1)}
        ways[0] = [[]]

        for candidate in candidates:
            for index in range(candidate, len(ways)):
                for combo in ways[index - candidate]:
                    newCombo = combo + [candidate]
                    ways[index].append(newCombo)

        return ways[target]

