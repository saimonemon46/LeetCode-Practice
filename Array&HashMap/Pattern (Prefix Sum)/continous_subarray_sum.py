class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """Brute Force:
                        for every subaray of length 2 and greater 
                            calculate its sum 
                            check if sum % k == 0 
                                if yes ---> true 
                            else ---> fasle
                                   
        """
        # for i in range(len(nums)):
        #     total = 0
        #     for j in range(i, len(nums)):
        #         total += nums[j]
                
        #         # check if total is multiple of k and subarray lenght 2 or greater
        #         if j-i+1>=2 and total % k == 0 :
        #             return True
        # return False
        
        """Optimal solution:
                            calculate prefix sum
                            each prefix sum % k --->
                                    store them with index
                                    
                                check if 2 remainder same and diff of index >= 2 
                                            yes --> true
                                            no --> fasle
        """
        
        # Remainder map with index
        remaindermap = {0: -1} # reamainder first index
        total = 0
        
        for i in range(len(nums)):
            # calculate prefix sum 
            total += nums[i]
            # caculate remainder
            remainder = total % k
            
            # check if remainder present in remainder map or not
            if remainder in remaindermap:
                # now check --> index diff ( must be >= 2)
                if i - remaindermap[remainder] >= 2:
                    return True
            # remainder not present ---> stpre with index
            else:
                remaindermap[remainder] = i
        
        return False    
        
        
        