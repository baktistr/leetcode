class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        output = []
        index = 0
        for num in nums:
            if num ==val:
                continue
            output.append(num)
        for i in range(len(output)):
            nums[i] = output[i]

        return len(output)