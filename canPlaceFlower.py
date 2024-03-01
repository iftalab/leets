from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(0,len(flowerbed)):
            if(n == 0):
                break
            if(i == 0 and flowerbed[i] == 0 and len(flowerbed) > 1 and flowerbed[i+1] == 0):
                n-=1
                flowerbed[i] = 1
            elif (i == len(flowerbed)-1 and flowerbed[i] == 0 and flowerbed[i-1] == 0):
                n-=1
                flowerbed[i] = 1
            elif(flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
                n-=1
                flowerbed[i] = 1
            
        return n == 0
            
        
s = Solution()
print(s.canPlaceFlowers([1,0,0,0,1],1))
print(s.canPlaceFlowers([1,0,0,0,1],2))
print(s.canPlaceFlowers([0,0,0,0,0],2))
print(s.canPlaceFlowers([0,0,0,0,0],3))
print(s.canPlaceFlowers([0,0,0,0,0],4))
print(s.canPlaceFlowers([0,1,0,0,0],1))
print(s.canPlaceFlowers([0,1,0,0,0],2))
print(s.canPlaceFlowers([0],1))
print(s.canPlaceFlowers([1],1))
print(s.canPlaceFlowers([0,1],1))
print(s.canPlaceFlowers([0,0],1))
print(s.canPlaceFlowers([0,0,0],2))
print(s.canPlaceFlowers([0,0,0,0,0,1,0,0],0))