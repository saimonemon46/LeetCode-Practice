"""
Problem : Top K most frequent elemants

Algo:
        count all the elements frequency and return top k frequency
"""
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dict 
        freq = {}
        
        # Count frequency
        for curr in nums:
            freq[curr] = freq.get(curr, 0) + 1
            
        # fetch top k frequncy using heapq
        topk = heapq.nlargest(k, freq.items(), key = lambda x: x[1])
        return [num for num, count in topk] # only keys List comprehension
        
        