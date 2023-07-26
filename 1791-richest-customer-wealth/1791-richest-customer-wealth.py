class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for i in range(len(accounts)):
            value = 0
            for j in range(len(accounts[i])):
                value = value + accounts[i][j]
            if (value > max):
                max = value
        return max