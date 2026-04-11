class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0 
        graph = defaultdict(set)
        for bus in routes:
            for i, stop in enumerate(bus): 
                for _ in bus:
                    graph[stop].add(_)
        

        from collections import deque 

        q = deque([source])
        print(graph)
        count = 0 
        visited = set() 
        while q:
            count+=1  
            for i in range(len(q)):
                node = q.popleft()
                visited.add(node)
                for d in graph[node]:
                    if d in visited:
                        continue
                    if d == target:
                        return count
                    else:
                        q.append(d)
        
        return -1
            
