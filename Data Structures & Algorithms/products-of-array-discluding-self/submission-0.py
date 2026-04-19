class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # n = len(nums)
        # output = []

        # for i in range(n):
        #     temp = 1
        #     for j in range(n):
        #         if i == j:
        #             continue                
        #         temp *= nums[j]
        #     output.append(temp)
        # return output

        # nums=[-1,0,1,2,3]
        n = len(nums)
        prefix = 1
        res = [1] * (n) # [1,-1,0,0,0] /  [0,-6,0,0,0]
        for i in range(n):
            res[i] = prefix
            prefix = prefix * nums[i]

        postfix = 1 
        for i in range(n-1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]

        return res