class Solution():
    def threesum(self, nums):
        x = []
        z = len(nums)
        for a in range(z-2):
            for b in range(a+1, z-1):
                for c in range(a+2, z):
                    if nums[a]+nums[b] + nums[c] == 0:
                        y = [nums[a], nums[b], nums[c]]
                        y.sort()
                        if y not in x:
                            x.append(y)
        return x


num = Solution()
nums = [-1, 0, 1, 2, -1, -4]
