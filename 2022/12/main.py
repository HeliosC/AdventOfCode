import sys

input = [line.replace("\n", "") for line in open("2022/12/input.txt", "r").readlines()]
#print(input)

def calculateWeight(node):
    match node:
        case 'S':
            return 1
        case 'E':
            return 26
        case _:
            return ord(node) - ord("a") + 1

def getNodeName(x, y):
    return str(x) + "-" + str(y)

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.keys())
    #print("unvisited_nodes", unvisited_nodes)
 
    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
    shortest_path = {}
 
    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}
 
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0
    
    a = 0
    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        a += 1
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            #print("node in unvisited_nodes", node)
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
            #print("current_min_node", current_min_node)

        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph[current_min_node]
        #print("neighbors", neighbors)
        for (neighbor, weight) in neighbors.items():
            #print("neighbor in neighbors.items()", neighbor, weight)
            tentative_value = shortest_path[current_min_node] + weight
            #print("tentative_value < shortest_path[neighbor]", tentative_value, shortest_path[neighbor])

            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
 
        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)

        if a == 3:
            continue
            return
    return previous_nodes, shortest_path
    
def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    # Add the start node manually
    path.append(start_node)
    
    #print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    #print(" -> ".join(reversed(path)))
    #print(len(path) - 1)
    return path

graph = {}
def firstHalf():
    for y, list in enumerate(input):
        for x, elevation in enumerate(list):
            nodeWeight = calculateWeight(elevation)
            nodes = {}

            for direction in range(4):
                xTarget = 0
                yTarget = 0
                match direction:
                    case 0:
                        xTarget = x + 1
                        yTarget = y

                    case 1:
                        xTarget = x
                        yTarget = y + 1

                    case 2:
                        xTarget = x - 1
                        yTarget = y

                    case 3:
                        xTarget = x
                        yTarget = y - 1

                if not (0 <= xTarget < len(list) and 0 <= yTarget < len(input)):
                    continue

                taget = input[yTarget][xTarget]
                tagetWeight = calculateWeight(taget)
                if (step := tagetWeight - nodeWeight) <= 1:
                    nodes[getNodeName(xTarget, yTarget)] = 1 #step

            graph[getNodeName(x, y)] = nodes

    #print(graph)

    S = ""
    E = ""

    for y, list in enumerate(input):
        for x, elevation in enumerate(list):
            if elevation == 'S':
                S = getNodeName(x, y)

            if elevation == 'E':
                E = getNodeName(x, y)

    #print(S, "->", E)

    #previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=S)
    #print("previous_nodes", previous_nodes)
    #print("shortest_path", shortest_path)

    #path = print_result(previous_nodes, shortest_path, start_node=S, target_node=E)




    minStart = ""
    minStep = sys.maxsize
    for y, list in enumerate(input):
        for x, elevation in enumerate(list):
            if(elevation != 'a'):
                continue

            start = getNodeName(x, y)
            print(start)
            previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=start)

            if E not in previous_nodes:
                continue

            path = print_result(previous_nodes, shortest_path, start_node=start, target_node=E)
            if (pathLen := len(path)) < minStep:
                minStart = start
                minStep = pathLen
                print("MIN", start, pathLen)
            
            print(pathLen)
    

    previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=minStart)
    path = print_result(previous_nodes, shortest_path, start_node=minStart, target_node=E)

    pathMap = [[' ' for _ in range(len(input[0]))] for _ in range(len(input))]
    for step in path:
        (x, y) = step.split("-")
        (x, y) = (int(x), int(y))
        pathMap[y][x] = input[y][x]

    for line in pathMap:
        print("".join(line))

    print(len(path) - 1)



firstHalf()