'''
Ссылка на описание задачи:
https://leetcode.com/problems/median-of-two-sorted-arrays/
'''
from numpy import median


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        med = median(nums)
        return med

