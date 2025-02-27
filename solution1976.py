class Solution(object):
    def countPaths(self, n, roads):
        
        times = {i: float("inf") for i in range(n)}
        times[0] = 0

        ways = {i: 0 for i in range(n)}
        ways[0] = 1

        graph = {i: [] for i in range(n)}

        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))

        min_heap = [(0, 0)]

        while min_heap:
            current_time, current_node = heapq.heappop(min_heap)

            if current_time > times[current_node]:
                continue

            for node, time in graph[current_node]:
                min_time = current_time + time

                if min_time < times[node]:
                    times[node] = min_time
                    ways[node] = ways[current_node]
                    heapq.heappush(min_heap, (min_time, node))

                elif min_time == times[node]:
                    ways[node] += ways[current_node]

        return ways[n - 1] % (10 ** 9 + 7)
       
       
        