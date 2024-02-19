class Solution:
    def trap(self, height):
        a = 0
        h = len(height)

        for i in range(1, h - 1):
            left_max = max(height[:i])
            right_max = max(height[i+1:])

            min_boundary = min(left_max, right_max)

            if min_boundary > height[i]:
                a += min_boundary - height[i]

        return a


A = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(A.trap(height))
