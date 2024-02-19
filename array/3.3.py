class Solution(object):
    def twoSum(self, nums, target):
        for x in range(len(nums)):
            sum = target - nums[x]
            if sum in nums:
                return (sum, nums[x])
        return (False)


A = Solution()
nums = [2, 7, 11, 15]
Target = 9
print(A.twoSum(nums, Target))
