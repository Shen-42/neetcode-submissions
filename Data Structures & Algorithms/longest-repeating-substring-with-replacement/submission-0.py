class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        c1 = [0] * 26
        left = 0
        longest_char_replacement = 0

        for right in range(len(s)):
            c1[ord(s[right])-ord("A")] += 1

            while (right - left + 1) - max(c1) > k:
                c1[ord(s[left]) - ord("A")] -= 1
                left += 1

            longest_char_replacement = max(longest_char_replacement, right - left + 1)
            
        return longest_char_replacement


