"""
Problem : Runnig sum

Algo:
        Build prefix
        
        prefix list ( can be empty or values with 0) 
        
        prefix[0] = nums[0] / prefix.append(nums[0]) ( append or insert)
        
        for the remainig elements
            prefix[i] = prefix[i-1] + nums[i]
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = []
        
        # first element same
        prefix.append(nums[0])
        
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] + nums[i])
            
        return prefix