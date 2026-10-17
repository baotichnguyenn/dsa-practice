
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = "".join(
            char.lower() for char in s if char.isalnum()
        )

        if len(clean_text) <= 1:
            return True

        result = clean_text[0] == clean_text[-1]

        return result and self.isPalindrome(clean_text[1:-1])
