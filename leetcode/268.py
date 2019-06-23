class Solution:
    def missingNumber(self, nums):
        sum = 0
        
        for i in range( len(nums)):
            sum += nums[i]
            
        actual = len(nums) * (len(nums) + 1) //2
        
        print( actual - sum)


s= Solution()

s.missingNumber([3,0,1])