class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        for i, num in enumerate(nums):
            print("ini num ",num)
            print("ini i ",i)
            if num >= target:
                return i

        return len(nums)
