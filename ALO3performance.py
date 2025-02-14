import time
import matplotlib.pyplot as plt
from Astar import for_all_combinations, a_star_search, heuristic

# this file runs the Astar algorithm on layout 3 (increased complexity)
# Refer to presentation file for visualization of the layout

# Example graph layout 3 (based on the provided structure)
graph = {'A_1': [('AA_1', 10), ('A_2', 10)], 'B_1': [('AB_1', 10), ('B_2', 10)], 'C_1': [('AC_1', 24), ('C_2', 10)], 'D_1': [('AD_1', 24), ('D_2', 10)], 'E_1': [('AG_1', 32), ('E_2', 10)], 'F_1': [('AE_1', 14), ('F_2', 10)], 'G_1': [('AF_1', 14), ('G_2', 10)], 'H_1': [('AF_1', 25), ('H_2', 10)], 'I_1': [('AJ_1', 15), ('I_2', 10)], 'J_1': [('AK_1', 19), ('J_2', 10)], 'K_1': [('AN_1', 15), ('K_2', 10)], 'L_1': [('AL_1', 12), ('L_2', 10)], 'M_1': [('AM_1', 12), ('M_2', 10)], 'N_1': [('AN_1', 12), ('N_2', 10)], 'AA_1': [('A_1', 10), ('AB_1', 34), ('AE_1', 21), ('AA_2', 10)], 'AB_1': [('AA_1', 34), ('AC_1', 34), ('B_1', 10)], 'AC_1': [('AB_1', 34), ('AD_1', 84), ('AH_1', 43), ('C_1', 24)], 'AD_1': [('AC_1', 84), ('AF_1', 21), ('D_1', 24)], 'AE_1': [('AA_1', 21), ('AG_1', 22), ('F_1', 14)], 'AF_1': [('AD_1', 21), ('AI_1', 22), ('G_1', 14), ('H_1', 25)], 'AG_1': [('AE_1', 22), ('AH_1', 68), ('AJ_1', 21), ('E_1', 32)], 'AH_1': [('AC_1', 43), ('AG_1', 68), ('AK_1', 21), ('AI_1', 84)], 'AI_1': [('AF_1', 22), ('AH_1', 84), ('AN_1', 47)], 'AJ_1': [('AG_1', 21), ('AL_1', 26), ('I_1', 15)], 'AK_1': [('AH_1', 21), ('AM_1', 26), ('J_1', 19)], 'AL_1': [('AJ_1', 26), ('AM_1', 68), ('L_1', 12)], 'AM_1': [('AK_1', 26), ('AL_1', 68), ('AN_1', 84), ('M_1', 12)], 'AN_1': [('AI_1', 47), ('AM_1', 84), ('N_1', 12), ('K_1', 15)], 'A_2': [('AA_2', 10), ('A_1', 10)], 'B_2': [('AB_2', 10), ('B_1', 10)], 'C_2': [('AC_2', 24), ('C_1', 10)], 'D_2': [('AD_2', 24), ('D_1', 10)], 'E_2': [('AG_2', 32), ('E_1', 10)], 'F_2': [('AE_2', 14), ('F_1', 10)], 'G_2': [('AF_2', 14), ('G_1', 10)], 'H_2': [('AF_2', 25), ('H_1', 10)], 'I_2': [('AJ_2', 15), ('I_1', 10)], 'J_2': [('AK_2', 19), ('J_1', 10)], 'K_2': [('AN_2', 15), ('K_1', 10)], 'L_2': [('AL_2', 12), ('L_1', 10)], 'M_2': [('AM_2', 12), ('M_1', 10)], 'N_2': [('AN_2', 12), ('N_1', 10)], 'AA_2': [('A_2', 10), ('AB_2', 34), ('AE_2', 21), ('AA_1', 10)], 'AB_2': [('AA_2', 34), ('AC_2', 34), ('B_2', 10)], 'AC_2': [('AB_2', 34), ('AD_2', 84), ('AH_2', 43), ('C_2', 24)], 'AD_2': [('AC_2', 84), ('AF_2', 21), ('D_2', 24)], 'AE_2': [('AA_2', 21), ('AG_2', 22), ('F_2', 14)], 'AF_2': [('AD_2', 21), ('AI_2', 22), ('G_2', 14), ('H_2', 25)], 'AG_2': [('AE_2', 22), ('AH_2', 68), ('AJ_2', 21), ('E_2', 32)], 'AH_2': [('AC_2', 43), ('AG_2', 68), ('AK_2', 21), ('AI_2', 84)], 'AI_2': [('AF_2', 22), ('AH_2', 84), ('AN_2', 47)], 'AJ_2': [('AG_2', 21), ('AL_2', 26), ('I_2', 15)], 'AK_2': [('AH_2', 21), ('AM_2', 26), ('J_2', 19)], 'AL_2': [('AJ_2', 26), ('AM_2', 68), ('L_2', 12)], 'AM_2': [('AK_2', 26), ('AL_2', 68), ('AN_2', 84), ('M_2', 12)], 'AN_2': [('AI_2', 47), ('AM_2', 84), ('N_2', 12), ('K_2', 15)]}


sequences = [
    ['B_1'],
    ['C_1', 'AC_1'],
    ['D_1', 'AD_1', 'AF_1'],
    ['E_1', 'AG_1', 'AJ_1', 'I_2'],
    ['F_1', 'AE_1', 'AG_1', 'AH_1', 'AK_1'],
    ['G_1', 'AF_1', 'AI_1', 'AN_1', 'K_2', 'K_1'],
    ['H_1', 'AF_1', 'AI_1', 'AN_1', 'N_2', 'M_1', 'AM_1'],
    ['I_1', 'AJ_1', 'AL_1', 'AM_1', 'AK_2', 'J_1', 'J_2', 'K_2'],
    ['J_1', 'AK_1', 'AH_1', 'AI_2', 'AN_2', 'M_2', 'L_2', 'L_1', 'AL_2']
]
execution_times = []
costs = []

# Start node
start_node = 'A_1'

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
