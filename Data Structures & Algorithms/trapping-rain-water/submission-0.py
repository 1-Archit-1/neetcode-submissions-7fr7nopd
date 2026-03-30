class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = 0
        locall = 0
        localr = 0
        localsl = []
        localsr = [None for _ in range(len(height))] 
        for i in range(len(height)):
            localsl.append(locall)
            if height[i] > locall:
                locall = height[i]

        for i in range(len(height)-1, -1, -1):
            localsr[i] = localr
            if height[i]>localr:
                localr = height[i]
        # print(localsl)
        # print(localsr)
        S= 0 
        for i in range(len(height)):
            locall = localsl[i]
            localr = localsr[i]
            hei = min(locall,localr)
            S+= max(hei - height[i], 0 )
        
        return S 