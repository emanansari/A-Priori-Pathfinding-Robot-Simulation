import itertools
import heapq

def shortest_path(graph, start_node, intermediate_nodes):
    n = len(intermediate_nodes)
    min_cost = float('inf')
    best_order = None
    best_path = []

    def calculate_path_cost(order):
        current_node = start_node
        total_cost = 0
        path = [start_node]
        
        for node in order:
            cost, intermediate_path = next_hop_cost(graph, current_node, node)
            total_cost += cost
            path.extend(intermediate_path[1:])  # Append intermediate path except the first node
            current_node = node
        
        # Return to start node
        cost, intermediate_path = next_hop_cost(graph, current_node, start_node)
        total_cost += cost
        path.extend(intermediate_path[1:])
        
        return total_cost, path

    def next_hop_cost(graph, current_node, next_node):
        if current_node == next_node:
            return 0, [current_node]
        
        # Directly return the weight if the edge exists
        for neighbor, weight in graph.get(current_node, []):
            if neighbor == next_node:
                return weight, [current_node, next_node]
        
        # If direct edge doesn't exist, use Dijkstra's algorithm to find the shortest path
        dist = {current_node: 0}
        prev = {current_node: None}
        priority_queue = [(0, current_node)]
        heapq.heapify(priority_queue)

        while priority_queue:
            current_dist, u = heapq.heappop(priority_queue)
            if u == next_node:
                break

            for neighbor, weight in graph.get(u, []):
                distance = current_dist + weight
                if neighbor not in dist or distance < dist[neighbor]:
                    dist[neighbor] = distance
                    prev[neighbor] = u
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        # Reconstruct path
        if next_node not in dist:
            return float('inf'), []
        
        path = []
        step = next_node
        while step is not None:
            path.insert(0, step)
            step = prev[step]
        
        return dist[next_node], path

    for order in itertools.permutations(intermediate_nodes):
        order = (start_node,) + order
        cost, path = calculate_path_cost(order)
        if cost < min_cost:
            min_cost = cost
            best_order = order
            best_path = path

    priv = None
    robot_input = []
    for element in best_path:
        if priv is not None:
            robot_input.append((priv, element))
        priv = element

    return best_order, best_path, min_cost, robot_input

# Example graph (based on the provided structure)

graph = {
    'A': [('AA', 10)],
    'B': [('AB', 10)],
    'C': [('AC', 24)],
    'D': [('AD', 24)],
    'E': [('AG', 32)],
    'F': [('AE', 14)],
    'G': [('AF', 14)],
    'H': [('AF', 25)],
    'I': [('AJ', 15)],
    'J': [('AK', 19)],
    'K': [('AN', 15)],
    'L': [('AL', 12)],
    'M': [('AM', 12)],
    'N': [('AN', 12)],
    'AA': [('A', 10), ('AB', 34), ('AE', 21)],
    'AB': [('AA', 34), ('AC', 34), ('B', 10)],
    'AC': [('AB', 34), ('AD', 84), ('AH', 43), ('C', 24)],
    'AD': [('AC', 84), ('AF', 21), ('D', 24)],
    'AE': [('AA', 21), ('AG', 22), ('F', 14)],
    'AF': [('AD', 21), ('AI', 22), ('G', 14), ('H', 25)],
    'AG': [('AE', 22), ('AH', 68), ('AJ', 21), ('E', 32)],
    'AH': [('AC', 43), ('AG', 68), ('AK', 21), ('AI', 84)],
    'AI': [('AF', 22), ('AH', 84), ('AN', 47)],
    'AJ': [('AG', 21), ('AL', 26), ('I', 15)],
    'AK': [('AH', 21), ('AM', 26), ('J', 19)],
    'AL': [('AJ', 26), ('AM', 68), ('L', 12)],
    'AM': [('AK', 26), ('AL', 68), ('AN', 84), ('M', 12)],
    'AN': [('AI', 47), ('AM', 84), ('N', 12), ('K', 15)]
}

# Example usage:

"""
best_order, best_path, min_cost, robot_input = shortest_path(graph, start_node, intermediate_nodes)
print("Best order to visit nodes:", best_order)
print("Best path including all intermediate nodes:", best_path)
print("Minimum path cost:", min_cost)
print(robot_input)
"""

