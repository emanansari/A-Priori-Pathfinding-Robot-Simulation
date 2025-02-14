import time
import matplotlib.pyplot as plt
from tsp2 import shortest_path

#this file runs the Dijstras algorithm on layout 1

# graph of first layout representing the distances/weights between each 
# node and it's connecting nodes
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

# list of arbitrary user inputs that represent table orders
# each element in this list is a different destination table
# so 'F' is a single table order where the robot has to simply find the shortest path to F
# sequences like ['E', 'M', 'C'] are multiple table orders and the robot must find the
# shortest path to each table keeping the cost to a minimum

sequences = [
    ['F'],
    ['L', 'C'],
    ['E', 'M', 'C'],
    ['N', 'J', 'D', 'H'],
    ['I', 'F', 'F', 'G', 'B'],
    ['N', 'M', 'C', 'K', 'H', 'J'],
    ['D', 'K', 'B', 'N', 'G', 'M', 'I'],
    ['F', 'L', 'G', 'I', 'K', 'J', 'M', 'H'],
    ['D', 'N', 'E', 'G', 'M', 'B', 'K', 'L', 'J']
]    
"""

    ['C', 'F', 'J', 'B', 'I', 'K', 'H', 'M', 'L', 'E'],
    ['B', 'M', 'G', 'D', 'F', 'N', 'H', 'I', 'L', 'K', 'C'],
    ['E', 'B', 'F', 'M', 'K', 'J', 'L', 'N', 'H', 'G', 'I', 'C'],
    ['C', 'K', 'L', 'M', 'N', 'J', 'H', 'E', 'D', 'B', 'G', 'F', 'I'],
    ['H', 'J', 'D', 'K', 'G', 'L', 'F', 'AC', 'N', 'E', 'C', 'B', 'M', 'I'],
    ['N', 'D', 'L', 'H', 'F', 'M', 'E', 'AD', 'C', 'J', 'B', 'K', 'G', 'I', 'AF'],
    ['B', 'E', 'AE', 'D', 'F', 'L', 'M', 'G', 'K', 'H', 'N', 'J', 'I', 'C', 'AC', 'F'],
    ['J', 'B', 'E', 'M', 'AE', 'D', 'N', 'K', 'H', 'G', 'I', 'L', 'F', 'C', 'AD', 'E', 'D'],
    ['L', 'G', 'N', 'K', 'AF', 'J', 'C', 'E', 'B', 'M', 'H', 'D', 'I', 'F', 'AC', 'N', 'L', 'J'],
    ['K', 'L', 'B', 'F', 'H', 'M', 'G', 'AI', 'E', 'N', 'C', 'J', 'I', 'D', 'AH', 'L', 'B', 'G', 'E'],
    ['N', 'G', 'D', 'E', 'L', 'H', 'B', 'C', 'K', 'J', 'I', 'AE', 'F', 'M', 'AG', 'L', 'G', 'D', 'C', 'K']
"""

# Initialize lists to store execution times and costs
execution_times = []
costs = []

# Start node
start_node = 'A'

# Run the algorithm for each sequence
for seq in sequences:
    start_time = time.time()
    best_order, best_path, min_cost, robot_input = shortest_path(graph, start_node, seq)
    end_time = time.time()
    
    execution_time = end_time - start_time
    execution_times.append(execution_time)
    costs.append(min_cost)
    print(robot_input)
    print("Best order to visit nodes:", best_order)
    print("Minimum path cost:", min_cost)

# Plotting the results
input_lengths = [len(seq) for seq in sequences]

# Plot execution time against input length
plt.figure(figsize=(12, 6))
plt.plot(input_lengths, execution_times, marker='o', linestyle='-', color='b')
plt.title('Execution Time vs Input Length')
plt.xlabel('Input Length')
plt.ylabel('Execution Time (seconds)')
plt.grid(True)
plt.savefig('execution_time_vs_input_length.png')  # Save plot to a file
plt.show()

# Plot cost against input length
plt.figure(figsize=(12, 6))
plt.plot(input_lengths, costs, marker='o', linestyle='-', color='r')
plt.title('Cost vs Input Length')
plt.xlabel('Input Length')
plt.ylabel('Cost')
plt.grid(True)
plt.savefig('cost_vs_input_length.png')  # Save plot to a file
plt.show()
