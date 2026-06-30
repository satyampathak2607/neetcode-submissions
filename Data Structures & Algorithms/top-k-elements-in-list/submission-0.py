class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1


        bucket = [[] for _ in range(len(nums) + 1)]
        for num in seen:
            freq= seen[num]
            bucket[freq].append(num)

        ans=[]

        for freq in range(len(bucket)-1,0,-1):
            for num in bucket[freq]:
                ans.append(num)


                if len(ans)==k:
                    return ans




        
        