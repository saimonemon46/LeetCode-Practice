class Solution:
    
    """
    Brute Force: 
                    check every subarray sum and compare 
                    
    Optimal: 
                    Use hashmap and Prefix sum pattern
                    
    """
    
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     count = 0
    #     for i in range(len(nums)):
    #         ## Sum  = 0 
    #         sum = 0
    #         for j in range(i, len(nums)):
    #             sum += nums[j]
    #             if sum == k:
    #                 count += 1
    #     return count
                
                
                
                
    """ Prefix sum """
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Calculate Prefix Sum 
        prefixsum = {0: 1} # 0 for single subarray ( element itself a subarray )
        total = 0 
        count = 0
        
        for i in nums:
            # count curr sum 
            total += i
            
            if total - k in prefixsum:
                # if total - k exists ---> a subarray exists ( count += frequency )
                count += prefixsum[total - k]
            
            
            # add currsum in prefix with frequency    
            prefixsum[total] = prefixsum.get(total, 0) + 1
        
        return count
                
        
        
        
        
        