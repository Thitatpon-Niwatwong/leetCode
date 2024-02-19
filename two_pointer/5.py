class Solution:
    def trap(self, height):
        a = 0
        h = len(height)
        for i in range(h):
            if height(i) < height(i-1) and height(i) < height(i+1):
                a = a + max(height(i + 1) - height(i),
                            height(i + 1) - height(1))
            if height(i) < height(i-1) and height(i) > height(i+1):
                a = a + height(i - 1) - height(i) + \
                    height(i - 1) - height(i + 1)
        return a


A = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(A.trap(height))
