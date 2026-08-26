class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        decoded = []
        i = 0
        
        while i < len(s):
            # Find the position of the length delimiter '#'
            j = s.find('#', i)
            length = int(s[i:j])
            
            # Extract the original string using the parsed length
            i = j + 1
            decoded.append(s[i:i + length])
            
            # Advance pointer to the start of the next string segment
            i += length
            
        return decoded