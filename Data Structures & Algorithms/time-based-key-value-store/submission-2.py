class TimeMap:

    def __init__(self):
        self.dictt = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictt[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        
        tup = self.dictt.get(key) 
        if not tup:
            return ""
        
        l = 0
        r = len(tup) - 1
        res = ""
        while l<=r: 
            mid = l+ (r-l)//2 
            if tup[mid][1] <= timestamp:
                res = tup[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res