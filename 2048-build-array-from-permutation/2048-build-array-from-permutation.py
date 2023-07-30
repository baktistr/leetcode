class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:

        # answer=[]
        # for i in range(len(nums)):
        #     # answer[i] = nums[nums[i]]
        #     answer.append(nums[nums[i]])
        # return answer

        # use meta value to modified existing array,  
        # because constraint problem : 1 < nums.length < 1000, Use cons = 1001
        # meta = a + cons_val*b  --> meta = nums[i]
        # a = meta % cons_val --> a = nums[i]
        # b = meta / cons_val --> b = nums[nums[i]] % cons_val

        # fill the meta value
        cons_val = 1001
        for i in range(len(nums)):
            # a = nums[i]
            b = nums[nums[i]]%cons_val
            nums[i] = nums[i] + b*cons_val

        # retrive the real value
        for i in range(len(nums)):
            nums[i] = nums[i]//cons_val

        return nums
