class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        if(n in self.memo):
            return self.memo[n]

        if(n <= 3):
            res = n
        else:
            res = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        self.memo[n] = res
        return res
        
        
        
        
