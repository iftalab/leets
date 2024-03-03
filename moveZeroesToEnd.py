from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(0, len(nums)):
            if(nums[i] == 0):
                j = i+1
                while j < len(nums) and nums[j] == 0:
                    j += 1
                if(j == len(nums)):
                    break
                nums[i] = nums[j]
                nums[j] = 0
    
    

s = Solution()
tc1 = [0,1,0,3,12]
s.moveZeroes(tc1)
print(tc1)

tc2 = [0]
s.moveZeroes(tc2)
print(tc2)
                
tc3 = [1]
s.moveZeroes(tc3)
print(tc3)

tc4 = [1,2,3]
s.moveZeroes(tc4)
print(tc4)

tc5 = [0,0,0]
s.moveZeroes(tc5)
print(tc5)

tc6 = [0,0,0,1]
s.moveZeroes(tc6)
print(tc6)

tc7 = [0,0,0,1,2]
s.moveZeroes(tc7)
print(tc7)
             