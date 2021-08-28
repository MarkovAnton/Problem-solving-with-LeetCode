'''
Ссылка на описание задачи:
https://leetcode.com/problems/valid-sudoku/
'''


class Solution(object):
    def isValidSudoku(self, board):
        n = 9
        nums = [str(i) for i in range(10)]
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]

        for r in range(n):
            for c in range(n):
                val = board[r][c]
                if val in nums:
                    if val in rows[r]:
                        return False
                    rows[r].add(val)

                    if val in cols[c]:
                        return False
                    cols[c].add(val)

                    idx = (r // 3) * 3 + c // 3
                    if val in boxes[idx]:
                        return False
                    boxes[idx].add(val)

        return True

