class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n]+=1 
        x = [[] for n in range(len(nums)+1)]
        for n,f in d.items():
            x[f].append(n)
        res =[]
        for i in range(len(x)-1,-1,-1):
            for nn in x[i]:
                res.append(nn)
                k-=1
                if k==0:
                    break
            if k==0:
                break
        return res