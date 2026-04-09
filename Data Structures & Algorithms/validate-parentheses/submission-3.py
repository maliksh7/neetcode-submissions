class Solution:
    def isValid(self, s: str) -> bool:
        
        opening = '([{'
        closing = ')]}'
        mapping = dict(zip(opening, closing))

        stack = []
        for char in s:
            if char not in mapping.values() and char not in mapping.keys():
                continue
            
            if char in mapping:
                stack.append(mapping[char])

            elif len(stack) == 0 or char != stack.pop():
                return False
        
        return len(stack) == 0
        