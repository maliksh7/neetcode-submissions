class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_nums = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hash_nums:
                return [hash_nums[diff], i]
            else:
                hash_nums[n] = i






        # n = nums[0]
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] and nums[j] < target:
        #             if nums[i] + nums[j] == target:
        #                 return [i, j]
                
                        
                