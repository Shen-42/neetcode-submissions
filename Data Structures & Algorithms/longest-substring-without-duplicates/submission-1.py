

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        left = 0
        window = set()
                
        for right in range(len(s)):

            while s[right] in window:
                window.remove(s[left])
                left += 1
            
            window.add(s[right])

            longest_substring = max(longest_substring, right - left + 1)

        return longest_substring
        


