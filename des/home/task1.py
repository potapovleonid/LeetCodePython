class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index_first_fig, first_fig in enumerate(nums):
            for index_second_fig, second_fig in enumerate(nums[index_first_fig + 1:]):
                if first_fig + second_fig == target:
                    return [index_first_fig, index_first_fig + index_second_fig + 1]


nums = [2, 7, 11, 15]
target = 9

s = Solution()

assert s.twoSum(nums, target) == [0, 1]

nums = [3, 2, 4]
target = 6

assert s.twoSum(nums, target) == [1, 2]
