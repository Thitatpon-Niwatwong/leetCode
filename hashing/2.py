class Solution(object):
    def isAnagram(self, s, t):
        Dict1 = {}
        Dict2 = {}
        for i in s:
            if i not in Dict1:
                Dict1[i] = 1
            else:
                Dict1[i] += 1
        for j in t:
            if j not in Dict2:
                Dict2[j] = 1
            else:
                Dict2[j] += 1
        return (Dict2 == Dict1)


A = Solution()
s = "anagram"
t = "nagaram"
print(A.isAnagram(s, t))
