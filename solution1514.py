class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):

        success = {i: 0 for i in range(n)}
        success[start_node] = 1
        graph = {i: [] for i in range(n)}
        max_heap = [(-1, start_node)]
        visited = set()

        for i in range(len(edges)):
            s, e = edges[i][0], edges[i][1]
            graph[s].append((e, succProb[i]))
            graph[e].append((s, succProb[i]))

        while max_heap:
            current_rate, current_node = heapq.heappop(max_heap)
            current_rate = -current_rate

            if current_node == end_node:
                return current_rate
            if current_node in visited:
                continue
            visited.add(current_node)

            for node, rate in graph[current_node]:
                max_rate = rate * current_rate
                if max_rate > success[node]:
                    success[node] = max_rate
                    heapq.heappush(max_heap, (-max_rate, node))

        return 0
      
      
        