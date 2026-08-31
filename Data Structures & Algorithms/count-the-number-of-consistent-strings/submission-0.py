class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allows = set(allowed)
        counter = 0
        for word in words:
            if set(word).issubset(allows):
                counter+=1
        return counter
