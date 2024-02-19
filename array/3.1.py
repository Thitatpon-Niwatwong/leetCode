class Solution(object):
    def twoSum(self, nums, target):
        num1 = []
        num2 = []
        for x in range(nums):
            num1 = num1.append(x)
            for y in range(nums):
                num2 = num2.append(y)
            if num1 + num2 == target and x != y:
                return (num1, num2)


a = Solution()
nums = [2, 7, 11, 15]
target = 9
print(a.twoSum(nums, target))
