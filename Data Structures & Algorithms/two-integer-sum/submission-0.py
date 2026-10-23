class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        answer = []
        
        for i, value in enumerate(nums):
 
            complement = target - nums[i]
            
            if complement in seen:
                answer.extend([seen[complement], i])
            
            seen[value] = i
        
        return answer


    
        