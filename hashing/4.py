class Solution(object):
    def groupAnagrams(self, strs):
        sum = {}
        for i in strs:
            new_sort = ''.join(sorted(i))
            if new_sort in sum:
                sum[new_sort].append(i)
            else:
                sum[new_sort] = [i]
        result = list(sorted(sum.values()))
        return (result)


A = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(A.groupAnagrams(strs))
