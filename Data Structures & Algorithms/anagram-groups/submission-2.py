class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        
        for s in strs:
            freq = [0] * 26

            for char in s:
                freq[ord(char) - ord("a")] += 1

            key = tuple(freq)      
            result[key] = result.get(key, []) + [s]

        return list(result.values())

        