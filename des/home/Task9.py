class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)
        return string == string[::-1]


s = Solution()
x = 121
assert s.isPalindrome(x) == True
