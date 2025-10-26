class Solution:
    
    # Function to return a list containing the DFS traversal of the graph.
    def dfs(self, V, adj):
        visited = [False] * V
        result = []

        # Define recursive helper function
        def dfsUtil(node):
            visited[node] = True     # Mark node as visited
            result.append(node)      # Add to traversal result

            # Visit all unvisited adjacent vertices
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    dfsUtil(neighbour)

        # Start DFS from vertex 0 (as per GFG convention)
        dfsUtil(0)

        return result
