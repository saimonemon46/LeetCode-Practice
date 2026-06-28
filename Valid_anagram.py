""" 
Problem : Valid Anagram

Algo:
     first if both s and t diff length 
        not anagram
        
     count both string occurance and compare ( using dict )
     if same : True (Anagram)
     if not same : False (Nor Anagram)
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # two dict for s and t
        sdict = {}
        tdict = {}
        
        for curr in s:
            sdict[curr] = sdict.get(curr, 0) + 1
        for curr in t:
            tdict[curr] = tdict.get(curr, 0) + 1
            
        # compare 
        return sdict == tdict