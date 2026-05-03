class Solution:
    def minCost(self, nums: list[int], q: list[list[int]]) -> list[int]:

        hs = defaultdict(set)

        hs[0].add(1)
        hs[len(nums) - 1].add(len(nums) - 2)
        for i in range(1, len(nums) - 1):
            mn = abs(nums[i] - nums[i - 1])
            mn1 = abs(nums[i] - nums[i + 1])

            if mn1 < mn:
                hs[i].add(i + 1)
            else:
                hs[i].add(i - 1)

        # print(hs)

        prefix = [0]
        sm = 0
        for i in range(len(nums) - 1):
            
            if i + 1 in hs[i]:
                sm += 1
            else:
                sm += abs(nums[i] - nums[i + 1])

            prefix.append(sm)


        suffix = [0]
        sm = 0
        for i in range(len(nums) - 1, 0, -1):
            
            if i - 1 in hs[i]:
                sm += 1
            else:
                sm += abs(nums[i] - nums[i - 1])

            suffix.append(sm)

        suffix = (suffix[::-1])

        ans = []

        for i, j in q:
            if i > j:
                ans.append(abs(suffix[j] - suffix[i]))
            else:
                ans.append(abs(prefix[j] - prefix[i]))

        return (ans)
            