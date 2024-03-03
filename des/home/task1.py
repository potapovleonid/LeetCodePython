class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index_first_fig in range(len(nums)):
            for index_second_fig in range(index_first_fig + 1, len(nums)):
                if nums[index_first_fig] + nums[index_second_fig] == target:
                    return [index_first_fig, index_second_fig]


nums = [2, 7, 11, 15]
target = 9

s = Solution()

assert s.twoSum(nums, target) == [0, 1]

nums = [3, 2, 4]
target = 6

assert s.twoSum(nums, target) == [1, 2]
