class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # string_x = str(x)
        # for i in range(len(string_x)):
        #     if string_x[i] == string_x[len(string_x)-1-i]:
        #         print(string_x[i])
        #         print(string_x[len(string_x)-1-i])
        #         continue
        #     else :
        #         return False
        # return True

        return str(x) == str(x)[::-1]
