class Solution:
    def productExceptSelf(self, nums):
        a = []
        for x in len(nums):
            c = 1
            for y in len(nums):
                if y != x:
                    c = c*nums[y]
            a = a.append(c)
        return (a)


A = Solution()
nums = [-1, 1, 0, -3, 3]
print(A.productExceptSelf(nums))
