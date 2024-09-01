from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = 0
        p2 = 0
        while p1 < (m+p2) and p2 < n:
           # print("p1 > ",p1, " num1[p1] > ", nums1[p1], " p2 > ", p2, " num2[p2] > ", nums2[p2])
            if(nums1[p1] > nums2[p2]):
                nums1.pop()
                nums1[p1:p1] = [nums2[p2]]
                p2 += 1
                p1 += 1
            else:
                p1 += 1
            #print("nums1 : ",nums1, " p1 : ", p1)
            #print("nums2 : ",nums2, " p2 : ", p2)
                
        while p2 < n:
            #print(p1)
            #print(nums2[p2])
            nums1.pop()
            nums1[p1:p1] = [nums2[p2]]
            p1 += 1
            p2 += 1
        return nums1
        
        
s = Solution()
print(s.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print(s.merge([2,5,6,0,0,0], 3,[1,2,3] , 3))
print(s.merge([1], 1, [], 0))
print(s.merge([0], 0, [1], 1))
print(s.merge([1], 1, [0], 0))