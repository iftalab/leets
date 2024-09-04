from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        print(nums)
        return len(nums)
s = Solution()
print(s.removeElement([3,2,2,3], 3))
print(s.removeElement([3,2,2,3], 2))
print(s.removeElement([0,1,2,2,3,0,4,2], 2))
print(s.removeElement([0,1,2,2,3,0,4,2], 1))