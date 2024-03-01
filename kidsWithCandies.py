from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for i in range(0, len(candies)):
            subject = candies[i] + extraCandies;
            isGreatest = True
            for j in range(0, len(candies)):
                isGreatest = isGreatest and subject >= candies[j]
                if(not isGreatest):
                    break
            result.append(isGreatest)
        return result
        
s = Solution()
print(s.kidsWithCandies([2,3,5,1,3], 3))
print(s.kidsWithCandies([4,2,1,1,2], 1))
print(s.kidsWithCandies([12,1,12], 10))
print(s.kidsWithCandies([1,1],1))
print(s.kidsWithCandies([3,1],1))
print(s.kidsWithCandies([3,10],10))