class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = ''
        result_substring = ''
        last_symbol = ''
        if len(s) == 0:
            return 0
        for j in range(0, len(s)):
            for i in s[j::]:
                if substring == '':
                    substring = i
                elif i in substring:
                    if len(substring) > len(result_substring):
                        result_substring = substring
                    substring = i
                elif result_substring != '' and i == last_symbol:
                    substring = i
                elif i != substring[-1]:
                    substring += i
                last_symbol = i
            if len(substring) > len(result_substring):
                result_substring = substring
            substring = ''
            last_symbol = ''
        return len(result_substring)


s = "abcabcbb"
s1 = "dvdf"
s2 = "pwwkew"
s3 = ' '
s4 = 'asjrgapa'

sol = Solution()
assert sol.lengthOfLongestSubstring(s) == 3
assert sol.lengthOfLongestSubstring(s1) == 3
assert sol.lengthOfLongestSubstring(s2) == 3
assert sol.lengthOfLongestSubstring(s3) == 1
assert sol.lengthOfLongestSubstring(s4) == 6
