from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums)-1:
            if(nums[i] == nums[i+1]):
                nums.remove(nums[i])
            else:
                i += 1
            
        return len(nums)
s = Solution()
print(s.removeDuplicates([1,1,2]))
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))