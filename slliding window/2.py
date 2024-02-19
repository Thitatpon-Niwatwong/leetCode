class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        maxlen = {}
        for a in range(n):
            if s == 0:
                maxlen[s[a]] = 1
            elif maxlen[a] not in maxlen.keys():
                maxlen[s[a]] += 1
            else:
                maxlen[s[a]] = 1
        return (max(maxlen.values()))


A = Solution()
s = "pwwkew"
print(A.lengthOfLongestSubstring(s))
