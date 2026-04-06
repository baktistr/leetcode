class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        hash_table = {}

        for i in range(n):
            hash_table[nums[i]] = i

        for i in range(n):
            complement = target - nums[i]
            if complement in hash_table and hash_table[complement] != i:
                return [i, hash_table[complement]]
        
        return []
        