class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []

        # use bruteforce, iterate i, and use two pointer (left & right) for each possible triplet with i
        # sort the nums, so we can move the two pointers accordingly
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums [i-1] : # skip for duplicate
                continue
            
            # two pointers
            left = i + 1
            right = len(nums) - 1

            # greedy for two pointer
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0 :# we need to find a bigger value, 
                    left += 1
                elif total > 0 :
                    right -= 1
                else :
                    result.append([nums[i], nums[left], nums[right]] )

                    # check another duplicate triplet
                    while left < right and nums[left] == nums[left+1]:
                        left += 1

                    left += 1
                    

        return result