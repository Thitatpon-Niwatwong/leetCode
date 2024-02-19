class Solution(object):
    def isValid(self, s):
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack


A = Solution()
s = "()"
print(A.isValid(s))
