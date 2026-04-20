# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         res = []
#         temp = nums[0] # ---> 2
#         final_res = []

#         for i in range(len(nums) - 1):
#             if nums[i+1] - nums[i] == 1:
#                 if nums[i] - temp == 1:
#                     res.append(temp)
#                 res.append(nums[i+1])
#                 temp = nums[i]
#             else:
#                 if len(res) > len(final_res):
#                     final_res = res
#                 res = []
#         print(final_res)
#         print(res)
#         return len(final_res)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


