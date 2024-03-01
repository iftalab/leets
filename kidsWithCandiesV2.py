from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        gretestCount = max(candies)
        for c in candies:
            result.append(c + extraCandies >= gretestCount)
        return result
        
s = Solution()
print(s.kidsWithCandies([2,3,5,1,3], 3))
print(s.kidsWithCandies([4,2,1,1,2], 1))
print(s.kidsWithCandies([12,1,12], 10))
print(s.kidsWithCandies([1,1],1))
print(s.kidsWithCandies([3,1],1))
print(s.kidsWithCandies([3,10],10))