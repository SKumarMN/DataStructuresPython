class Solution:
    def productExceptSelf(self, nums):
        
        length = len(nums)
        
        L, R , A = [0]* length, [0]*length, [0]*length
        
        
        #calculate left
        
        L[0] = 1
        
        for i in range(1, length):
            
            L[i]= L[i-1] * nums[i-1]
            
            
        
        R =1
        
        for i in reversed(range(length)):
            L[i] = R * L[i]
            R = R * nums[i]
            
            
        return L

x = Solution()

x.productExceptSelf([1,2,3,4])