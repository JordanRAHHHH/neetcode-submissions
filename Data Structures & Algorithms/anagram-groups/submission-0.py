class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = {}
        for i in range(len(strs)):
            if "".join(sorted(strs[i])) in seen:
                seen["".join(sorted(strs[i]))].append(strs[i]) 
            else:
                seen["".join(sorted(strs[i]))] = [strs[i]]
    
        return list(seen.values())

