class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result= defaultdict(list) #creates a special dictionary which creates empty list for new key if it comes

        for s in strs:
            sortedS = ''.join(sorted(s))# creates temp string for the current s sorts it in pieces  and then  joins it like "eat" to 'a','e','t' and finally to "aet"
            result[sortedS].append(s) #adds the s from og array to its respective key block and if that key block doesnt exists then with defaultdict creates one and adds it to that block 

        return list(result.values())    # returns the output as list of lists subgrouped lists ...the elements in the same key block gets into same group

        
            
        