class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ##  Pattern ---> Frequency Counting
        """
        Problem : Two Sum

        Algo:
            1. traverse through the list and keep doing this 
                need = target - current 
                
                check --> if need is stored in the hashmap or not 
                    if not ---> store the value in hashmap with index
                    if yes ---> retuen index of need and curr
        """


        # Empty dict
        seen = {}
        
        # loop through list and find need = target - curr
        for index, curr in enumerate(nums):
            need = target - curr
            
            # check if need is present in dict or not
            if need in seen:
                # return index of need and curr
                return(seen[need], index)
            
            # store curr with index in dict 
            seen[curr] = index