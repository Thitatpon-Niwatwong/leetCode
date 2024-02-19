class Solution():
    def maxArea(self, height):
        max_sum = 0
        c = len(height)
        for x in range(c-1):
            for y in range(x, c):
                sum = (y-x)*(min(height[x], height[y]))
                max_sum = max(max_sum, sum)
        return max_sum


A = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(A.maxArea(height))
