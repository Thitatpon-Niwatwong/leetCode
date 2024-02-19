class Solution():
    def isAnagram(self, s, t):
        a = sorted(s)
        b = sorted(t)
        if a == b:
            return True
        return False


A = Solution()
s = "rat"
t = "car"
print(A.isAnagram(s, t))
