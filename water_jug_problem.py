#slip5_2
#write a program to implement the Water JUg problem
from collections import deque

def water_jug_problem_trace_path(jug1_capacity, jug2_capacity, target):
    queue = deque([((0, 0), [(0, 0)])])
    visited = set()
    visited.add((0, 0))

    while queue:
        (jug1, jug2), path = queue.popleft()

        if jug1 == target or jug2 == target:
            return path

        possible_states = [
            (jug1_capacity, jug2),  
            (jug1, jug2_capacity), 
            (0, jug2),              
            (jug1, 0),           
            (max(0, jug1 - (jug2_capacity - jug2)), 
             min(jug2_capacity, jug1 + jug2)),  
            (min(jug1_capacity, jug1 + jug2), 
             max(0, jug2 - (jug1_capacity - jug1))) 
        ]

        for new_jug1, new_jug2 in possible_states:
            new_state = (new_jug1, new_jug2)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [new_state]))

    return None 
    
result = water_jug_problem_trace_path(4, 3, 2)

if result:
    print("Path to target:", result)
else:
    print("No solution found.")
