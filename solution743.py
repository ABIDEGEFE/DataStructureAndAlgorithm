class Solution(object):
    def networkDelayTime(self, times, n, k):
                
        graph = {i: [] for i in range(1, n+1)}
        for src, dis, time in times:
            graph[src].append((dis, time))

        distance = {i: float("inf") for i in range(1, n+1)}
        distance[k] = 0

        min_heap = [(0, k)]

        while min_heap:
            cur_time, cur_node = heapq.heappop(min_heap)

            if cur_time > distance[cur_node]:
                continue

            for dis, time in graph[cur_node]:
                length = cur_time + time
                if length < distance[dis]:
                    distance[dis] = length
                    heapq.heappush(min_heap, (length, dis))

        if max(distance.values()) < float("inf"):
            return max(distance.values())
        return -1
        