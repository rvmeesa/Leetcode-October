class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        
        # Reverse each word and store them in a list
        reversed_words = [word[::-1] for word in words]
        
        # Join the reversed words to form the final sentence
        result = ' '.join(reversed_words)
        
        return result
