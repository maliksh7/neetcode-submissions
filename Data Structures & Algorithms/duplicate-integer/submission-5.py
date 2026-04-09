class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_num = set()
        for num in nums:
            if num in hash_num:
                return True
            else:
                hash_num.add(num)
        return False