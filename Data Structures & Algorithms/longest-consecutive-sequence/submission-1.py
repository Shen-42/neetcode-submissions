class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        unique_nums = set(nums)

        for num in unique_nums:
            if num - 1 not in unique_nums:
                current = num
                current_length = 1

                while current + 1 in unique_nums:
                    current += 1
                    current_length += 1

                max_length = max(max_length, current_length)
            
      
        return max_length