class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n
        result = [1] * n

        left_product = 1
        for i in range(n):
            left_products[i] = left_product
            left_product *= nums[i]
            print(left_product)
            print(i)
            print(f"lefproduct is { left_product}")

        right_product = 1
        for i in range(n - 1, -1, -1):
            right_products[i] = right_product
            right_product *= nums[i]
            print(i)
            print(f"rightproduct is { right_product}")

        for i in range(n):
            result[i] = left_products[i] * right_products[i]

        return result


A = Solution()
nums = [1, 2, 3, 4]
print(A.productExceptSelf(nums))
