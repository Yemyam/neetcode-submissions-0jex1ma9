import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = [0] * len(nums)
        postfix_products = [0] * len(nums)
        # compute prefix products
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            prefix_products[i] = product
            
        # compute postfix products 
        print(postfix_products)
        product = 1
        for i in range(len(nums)-1, -1, -1):
            product *= nums[i]
            postfix_products[i] = product

        print(prefix_products, postfix_products)

        out = []
        for i in range(len(nums)):
            if i == 0:
                out.append(postfix_products[i+1])
            elif i == len(nums)-1:
                out.append(prefix_products[i-1])
            else:
                out.append(prefix_products[i-1] * postfix_products[i+1])
        return out
        