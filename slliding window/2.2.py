class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        maxlen = {}  # Dictionary to store character counts
        max_length = 0  # Variable to store the maximum substring length
        start = 0  # Starting index of the current substring

        for end in range(n):
            if s[end] not in maxlen or maxlen[s[end]] < start:
                maxlen[s[end]] = end
            else:
                start = maxlen[s[end]] + 1
                maxlen[s[end]] = end

            max_length = max(max_length, end - start + 1)

        return max_length


A = Solution()
s = "pwwkew"
print(A.lengthOfLongestSubstring(s))
