"""
Problem: Contains Duplicates

Algo:
      traverse through the list 
      
      check each curr exists in the dict or not 
      if not exists ---> store with
      if exists --> return true
      
      if not exists till the end of the list 
         return false
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Dict
        dict = {}
        
        for curr in nums:
            # checks curr exists in the dict or not
            if curr in dict:
                return True
            else:
                dict[curr] = dict.get(curr, 0) + 1
        return False