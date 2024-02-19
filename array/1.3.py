class Solution:
    def containsDuplicate(self, nums):
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

solution = Solution()
nums = [1, 2, 3, 1]
print(solution.containsDuplicate(nums))