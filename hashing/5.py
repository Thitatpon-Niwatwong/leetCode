class Solution(object):
    def topKFrequent(self, nums, k):
        a = {}
        b = []
        for i in nums:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        nums2 = sorted(a, key=a.get, reverse=True)
        for j in range(k):
            b.append(nums2[j])
        return (b)


A = Solution()
nums = [4, 1, -1, 2, -1, 2, 3]
k = 2
print(A.topKFrequent(nums, k))
