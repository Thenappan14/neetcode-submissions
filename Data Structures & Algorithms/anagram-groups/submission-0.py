class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)

        for alpha in strs:
            count = [0] * 26

            for occurence in alpha:
                count[ord(occurence) - ord("a")] += 1

            result[tuple(count)].append(alpha)

        return list(result.values())

        

            
            
        
        