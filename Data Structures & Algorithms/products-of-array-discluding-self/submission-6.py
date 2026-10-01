class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = [0] * len(nums)
        postfix_products = [0] * len(nums)
        prefix_product = 1
        postfix_product = 1
        for i in range(len(nums)):
            prefix_product *= nums[i]
            postfix_product *= nums[len(nums) - 1 - i]
            prefix_products[i] = prefix_product
            postfix_products[len(nums) - 1 - i] = postfix_product
        
        out = []
        for i in range(len(nums)):
            if i == 0:
                out.append(postfix_products[1])
            elif i == len(nums) - 1:
                out.append(prefix_products[len(nums) - 2])
            else:
                out.append(prefix_products[i - 1] * postfix_products[i + 1])
        return out
        