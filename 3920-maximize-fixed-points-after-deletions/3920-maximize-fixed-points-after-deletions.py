class Solution:
    def maxFixedPoints(self, nums: list[int]) -> int:

        sl=SortedList()
        n=len(nums)

        for i in range(n):
            val=nums[i]
            if i>=val:
                sl.add((i-val,val))

        lis=[]

        for de,val in sl:

            ind=bisect.bisect_left(lis,val)

            if ind==len(lis):
                lis.append(val)
            else:
                lis[ind]=val
        return len(lis)
            