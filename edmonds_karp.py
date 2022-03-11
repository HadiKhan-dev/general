import copy
from collections import deque

def edmonds_karp(entrances, exits, path):
    enterances_node_path = []
    for i in range(len(path)+2):
        if i-1 in entrances:
            enterances_node_path.append(2000000)
        else:
            enterances_node_path.append(0)
    new_path = [enterances_node_path]
    for i in range(1,len(path)+1):
        cur_row = path[i-1]
        if i-1 in exits:
            addit = [2000000]
        else:
            addit = [0]
        cur_row = [0]+cur_row+addit
        new_path.append(cur_row)

    new_path.append([0]*(len(path)+2))
    
    path = new_path
    
    max_flow = 0

    residual_network = copy.deepcopy(path)
    
    
    done = False
    
    while not done:
        done_path_find = False
        start_node = (0,[])
        hit_nodes = set([0])
        nodes_to_visit = deque([])
        while not done_path_find:
        
            for j in range(len(residual_network[start_node[0]])):
                if j not in hit_nodes and residual_network[start_node[0]][j] > 0:
                    new_node = (j,start_node[1]+[start_node[0]])
                    nodes_to_visit.append(new_node)
                    hit_nodes.add(new_node[0])
                
                    if j == len(path)-1:
                        found_path = new_node[1]+[j]
                        done_path_find = True

            if len(nodes_to_visit) == 0:
                found_path = None
                done_path_find = True
                break
        
            start_node = nodes_to_visit.popleft()
        
        
        if found_path == None:
            done = True
            break
        
        path_flow = float("inf")
        
        for i in range(len(found_path)-1):
            path_flow = min(path_flow,residual_network[found_path[i]][found_path[i+1]])

        max_flow += path_flow
        
        for i in range(len(found_path)-1):
            lo = found_path[i]
            hi = found_path[i+1]
            
            residual_network[lo][hi] = residual_network[lo][hi]-path_flow
            residual_network[hi][lo] = residual_network[hi][lo]+path_flow
    return max_flow
            
            
            
            
print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))