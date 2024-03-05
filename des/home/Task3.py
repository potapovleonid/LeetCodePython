class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        list1 = []
        max1 = 0
        for letter in s:
            if letter not in list1:
                list1.append(letter)
                max1 = max(max1, len(list1))
            elif letter in list1:
                sep = letter
                thing = "".join(list1)
                list2, sep, list1 = thing.partition(sep)
                list1 = list(list1)
                list1.append(letter)
        return max1


s = "abcabcbb"
s1 = "dvdf"
s2 = "pwwkew"
s3 = ' '
s4 = 'asjrgapa'
s5 = 'bbbbbb'

sol = Solution()
assert sol.lengthOfLongestSubstring(s) == 3
assert sol.lengthOfLongestSubstring(s1) == 3
assert sol.lengthOfLongestSubstring(s2) == 3
assert sol.lengthOfLongestSubstring(s3) == 1
assert sol.lengthOfLongestSubstring(s4) == 6
assert sol.lengthOfLongestSubstring(s5) == 1
