class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Fixed-size array for 26 lowercase letters
        counts = [0] * 26
        
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1
            
        # If any count isn't 0, s and t are not anagrams
        return all(c == 0 for c in counts)