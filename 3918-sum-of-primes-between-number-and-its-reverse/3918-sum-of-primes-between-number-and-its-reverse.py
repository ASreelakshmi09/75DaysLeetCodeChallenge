class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        def prime_rng(n=1001):
            p=[True for i in range(n)]
            i=2
            while i<n:
                if p[i]:
                    j=i*2
                    while j<n:
                        p[j]=False
                        j += i
                i += 1
            ans=[0 for i in range(n)]
            for i in range(2,n):
                if p[i]:
                    ans[i] = i
                ans[i] += ans[i-1]
            return ans
                
        
        r=0
        x=n
        while x:
            rem=x%10
            r *= 10
            r += rem
            x=x//10
        st,end=min(n,r)-1,max(n,r)
        prime=prime_rng(end+1)
        return prime[end]-prime[st]