import time
import matplotlib.pyplot as plt
from Astar import for_all_combinations, a_star_search, heuristic

# this file runs the Astar algorithm on layout 2 (increased complexity)
# refer to presentation file to see a visualization of this layout

# Example graph layout 2 of weights between nodes and connecting nodes 
graph = {
    'AE_1': [('AG_1', 22), ('F_1', 14)],
    'AF_1': [('AI_1', 22), ('H_1', 25), ('AF_2', 30)],
    'AG_1': [('AE_1', 22), ('AJ_1', 21)],
    'AI_1': [('AF_1', 22), ('AN_1', 47), ('AI_2', 30)],
    'AJ_1': [('AG_1', 21), ('AL_1', 26)],
    'AL_1': [('AJ_1', 26), ('L_1', 12)],
    'AN_1': [('AI_1', 47), ('N_1', 12), ('K_1', 15), ('AN_2', 30)],
    'E_2': [('AG_2', 32)],
    'F_1': [('AE_1', 14)],
    'G_2': [('AF_2', 14)],
    'L_1': [('AL_1', 12), ('L_2', 30), ('N_2', 84)],
    'N_1': [('AN_1', 12), ('N_2', 30)],
    'AE_2': [('AG_2', 22)],
    'AF_2': [('AI_2', 22), ('G_2', 14), ('AF_1', 30)],
    'AG_2': [('AE_2', 22), ('AH_2', 68), ('AJ_2', 21), ('E_2', 32)],
    'AH_2': [('AG_2', 68), ('AK_2', 21), ('AI_2', 84)],
    'AI_2': [('AF_2', 22), ('AH_2', 84), ('AN_2', 47), ('AI_1', 30)],
    'AJ_2': [('AG_2', 21), ('AL_2', 26)],
    'AK_2': [('AH_2', 21), ('AM_2', 26)],
    'AL_2': [('AJ_2', 26), ('AM_2', 68), ('L_2', 12)],
    'AM_2': [('AK_2', 26), ('AL_2', 68), ('AN_2', 84), ('M_2', 12)],
    'AN_2': [('AI_2', 47), ('AM_2', 84), ('N_2', 12), ('AN_1', 30)],
    'H_1': [('AF_1', 25)],
    'K_1': [('AN_1', 15)],
    'L_2': [('AL_2', 12), ('L_1', 30)],
    'M_2': [('AM_2', 12)],
    'N_2': [('AN_2', 12), ('N_1', 30), ('L_1', 84)]
}


sequences = [
    ['AG_2'],
    ['AG_1', 'AH_2'],
    ['AI_1', 'AF_1', 'H_1'],
    ['AN_2', 'AJ_2', 'AL_2', 'L_2'],
    ['AG_2', 'E_2', 'AG_2', 'AH_2', 'AI_2'],
    ['AE_2', 'AG_2', 'AH_2', 'AI_2', 'AN_2', 'N_2'],
    ['AJ_2', 'AG_2', 'AH_2', 'AI_2', 'AN_2', 'N_2', 'L_1'],
    ['AL_2', 'AF_2', 'AI_2', 'AN_2', 'N_2', 'L_1', 'AL_1', 'AJ_1'],
    ['AG_1', 'AF_1', 'AI_1', 'AN_1', 'N_1', 'L_1', 'AL_1', 'AJ_1', 'AM_2'],
]

execution_times = []
costs = []

# Start node
start_node = 'AE_1'

# Run the algorithm for each sequence
for seq in sequences:
    start_time = time.time()
    best_path, min_cost = for_all_combinations(seq)
    end_time = time.time()
    
    execution_time = end_time - start_time
    execution_times.append(execution_time)
    costs.append(min_cost)
    print(seq)
    print("Best order to visit nodes:", best_path)
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
