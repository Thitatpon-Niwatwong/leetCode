class Solution:
    def containDuplicate(self, nums):
        a = set()
        for i in nums:
            if i in a:
                return (True)
            a.add(i)
        return (False)


A = Solution()
nums = [1, 2, 3, 1]
print(A.containDuplicate(nums))
