class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in (range(0, n)):
            if len(nums1) == 0:
                return
            nums1[m + i] = nums2[i]
        nums1.sort()


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

s = Solution()
s.merge(nums1, m, nums2, n)

assert nums1 == [1, 2, 2, 3, 5, 6]
