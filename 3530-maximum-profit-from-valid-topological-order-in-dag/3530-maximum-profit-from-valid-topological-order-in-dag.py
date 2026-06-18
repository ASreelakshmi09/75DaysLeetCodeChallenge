class Solution:
        def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
            need = [0] * n
            for i, j in edges:
                need[j] |= (1 << i)    
            dp = [-1] * (1 << n)
            dp[0] = 0 
            for mask in range(1 << n):
                if dp[mask] == -1:
                    continue
                pos = mask.bit_count() + 1
                for i in range(n):
                    if (mask >> i) & 1 == 0: 
                        if (mask & need[i]) == need[i]: 
                            mask2 = mask | (1 << i)
                            dp[mask2] = max(dp[mask2], dp[mask] + score[i] * pos)
            return dp[(1 << n) - 1]