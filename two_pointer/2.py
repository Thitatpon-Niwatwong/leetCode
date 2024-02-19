class Solution(object):
    def twoSum(self, numbers, target):
        for x in range(len(numbers)):
            for y in range(len(numbers)):
                if numbers[y] == target - numbers[x] and x != y:
                    return (x, y)
        return False


A = Solution()
target = 9
numbers = [2, 7, 11, 15]
print(A.twoSum(numbers, target))
