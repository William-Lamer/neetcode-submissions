class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = [[]]
        map = defaultdict(list)
        for str in strs:
            arr = [0]*26
            for char in str:
               arr[ord(char)-97] += 1 
            map[tuple(arr)].append(str) 
        print(map)
        

        
        return list(map.values())