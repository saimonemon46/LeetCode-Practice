class NumArray:
    """
    Problem : Ranger sum Queries
    
    Algo:
            Multiple queries ---> prefix sum
            
            here , 
                    we know prefix[5] --> sum of 0 to 5
                    so , sum of 2 to 5 --> prefix[5] - prefix[1]
    """
    

    def __init__(self, nums: List[int]):
        
        # empty list
        self.prefix = []
        
        self.prefix.append(nums[0])
        
        for i in range(1, len(nums)):
            self.prefix.append(self.prefix[i-1] + nums[i])
        

    def sumRange(self, left: int, right: int) -> int:

        # find sum
        if left==0:
            return self.prefix[right]
        
        return self.prefix[right] - self.prefix[left - 1]