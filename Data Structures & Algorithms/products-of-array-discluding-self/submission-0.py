#Using Division Method
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Count zeros and find product of non-zero numbers
        zeros = nums.count(0)
        
        # Scenario 3: More than one zero means everything is zero
        if zeros > 1:
            return [0] * len(nums)
        
        # Calculate product of all non-zero elements
        total_prod = 1
        for x in nums:
            if x != 0:
                total_prod *= x
                
        result = []
        for x in nums:
            if zeros == 1:
                # Scenario 2: One zero exists
                # Only the position with the zero gets the total product
                result.append(total_prod if x == 0 else 0)
            else:
                # Scenario 1: No zeros
                # Use integer division (//) to avoid float conversion
                result.append(total_prod // x)
                
        return result
        

        
        
        