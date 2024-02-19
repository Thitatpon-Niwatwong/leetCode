class Solution(object):
    def twoSum(self, nums, target):
        for x in range(len(nums)):
            for y in range(x + 1, len(nums)):
                if nums[x] + nums[y] == target:
                    return (x, y)
                else:
                    return False


a = Solution()
nums = [2, 7, 11, 15]
target = 9
print(a.twoSum(nums, target))
