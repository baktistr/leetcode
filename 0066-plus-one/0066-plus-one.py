class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strings = ""
        for i in digits:
            strings += str(i)
        
        temp = str(int(strings)+1)

        return [int(temp[i]) for i in range (len(temp))]