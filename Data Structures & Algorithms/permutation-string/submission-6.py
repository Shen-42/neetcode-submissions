class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        k = len(s1)
        n = len(s2)
        left = 0

        c1 = [0] * 26
        c2 = [0] * 26

        if k > n:
            return False

        for i in range(len(s1)):
            c1[ord(s1[i]) - ord("a")] += 1
            c2[ord(s2[i]) - ord("a")] += 1
        
        if c1 == c2:
            return True

        for right in range(k,n):
            c2[ord(s2[right]) - ord("a")] += 1
            c2[ord(s2[left]) - ord("a")] -= 1

            if c1 == c2:
                return True
            
            left += 1
        
        return False

