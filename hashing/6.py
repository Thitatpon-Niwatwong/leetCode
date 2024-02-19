class Solution(object):
    def productExceptSelf(self, nums):
        sum = len(nums)
        a = [1]*sum
        b = [1]*sum
        for i in range(1, sum):
            a[i] = a[i-1]*nums[i-1]
        for j in range(sum-2, -1, -1):
            b[j] = b[j+1]*nums[j+1]

        result = [a*b for a, b in zip(a, b)]
        return (result)


A = Solution()
nums = [1, 2, 3, 4]
print(A.productExceptSelf(nums))
