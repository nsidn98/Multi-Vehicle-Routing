"""
    Create a random graph of locations and use minizinc
    to solve the multi-vehicle routing problem
    Minizinc code(.mzn file) taken from:
    http://www.dcs.gla.ac.uk/~pat/cpM/minizincCPM/vrp/model1/cvrp.mzn
"""
import argparse
import random
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import networkx as nx
from minizinc import Instance, Model, Solver

parser = argparse.ArgumentParser(description='MVRP Minizinc Test')
parser.add_argument('--num_cust', type=int, default=8,
                    help='Number of customers')
parser.add_argument('--num_vehicles', type=int, default=10,
                    help='Number of vehicles available')
parser.add_argument('--vehicle_capacity', type=int, default=30,
                    help='Capacity of each vehicle')
parser.add_argument('--np_seed', type=int, default=10,
                    help='Seed for numpy')
parser.add_argument('--rand_seed', type=int, default=96,
                    help='Seed for random library')

args = parser.parse_args()

# seed so that random graph and choice of edge colours is always same
random.seed(args.rand_seed)
np.random.seed(args.np_seed)
####################################################

# define parameters for the problem
num_cust = args.num_cust                        # number of nodes nodes
max_num_vehicles = args.num_vehicles            # number of vehicles available
max_vehicle_capacity = args.vehicle_capacity    # capacity each vehicle can take
demands = np.random.randint(1,max_vehicle_capacity,num_cust-1,int)  # demands at each node
demands = np.concatenate((demands,np.array([0]))) # add zero to the last node which is the depot
demands = [int(d) for d in demands] # because minizinc does not accept np.int64, have to explicitly convert to int
####################################################
# colours available in matplotlib
colours_list = list(mcolors.cnames.keys())
# create a node class
class Node:
    def __init__(self,name=None, pos=None, grid_size=100):
        self.name = name
        self.pos = pos
        if pos == None:
            self.pos = tuple(np.random.randint(0,grid_size,2))
        
    def distance(self, node):
        pos1 = np.array(self.pos)
        pos2 = np.array(node.pos)
        return int(np.linalg.norm(pos1-pos2))
####################################################
# create a random graph with random node positions
colors = random.sample(colours_list,max_num_vehicles)
node_names = []
node_labels = {}
nodes = []
pos = {}
for i in range(num_cust):
    node = Node(name=i+1)
    nodes.append(node)
    node_labels[i+1] = str(i+1)
    node_names.append(node.name)
    pos[i+1] = node.pos
####################################################
# create distance matrix
dist = np.zeros((num_cust,num_cust))
for i in range(num_cust):
    for j in range(num_cust):
        dist[i,j] = nodes[i].distance(nodes[j])
dist = dist.astype(int)
dist = dist.tolist()

# print the problem parameters
print('#'*50)
print(f'Number of customers are: {num_cust}')
print(f'Demands at each node are: {demands}')
print(f'Number of vehicles available: {max_num_vehicles}')
print(f'Maximum capacity of each vehicle: {max_vehicle_capacity}')
print('#'*50)
print()
####################################################
# initialise the Minizinc solver
gecode = Solver.lookup("gecode")

problem = Model()
# write the minizinc(.mzn) file here
problem.add_string(
    """
    include "globals.mzn";
    int: n; % Number of customers
    int: m; % Maximum number of vehicles
    int: DEPOT = n+1;
    set of int: CUSTOMERS = 1..n+1;
    set of int: NOTDEPOT = 1..n; % all customers, depot excluded
    set of int: VEHICLES = 1..m;
    set of int: CAPACITY = 0..capacity;

    int: capacity; % Capacity of each vehicle
    array[CUSTOMERS,CUSTOMERS] of int: distance; % Distance between customers
    array[CUSTOMERS] of int: demand; % Demand of each customer
    % array[CUSTOMERS] of int: service; % Service time
    % array[CUSTOMERS] of int: ready_time; % Time window for each customer (ignored here)
    % array[CUSTOMERS] of int: due_time; % Time window for each customer (ignored here)

    array[VEHICLES,CUSTOMERS] of var CUSTOMERS: succ; % succ[v,c] is customer vehicle v visits after customer c
    array[VEHICLES] of var CAPACITY: load; % load[v] is demand satisfied by vehicle v
    var VEHICLES: vehiclesUsed; 
    var int: distanceTravelled;

    constraint forall(v in VEHICLES)(subcircuit(row(succ,v)));
    constraint forall(v in VEHICLES,c in NOTDEPOT)(succ[v,DEPOT] = DEPOT -> succ[v,c] = c);
    constraint forall(c in NOTDEPOT)(count_eq(col(succ,c),c,m-1));
    constraint forall(v in VEHICLES)(load[v] = sum(c in NOTDEPOT)(if (succ[v,c] = c) then 0 else demand[c] endif));
    constraint vehiclesUsed = sum(v in VEHICLES)(succ[v,DEPOT] != DEPOT);
    constraint distanceTravelled = sum(v in VEHICLES,c in CUSTOMERS)(distance[c,succ[v,c]]);

    constraint forall(v in 1..m-1)(lex_greatereq(row(succ,v),row(succ,v+1))); % symmetry break
    %constraint forall(v in 1..m-1)(load[v] >= load[v+1]); % symmetry break

    solve::int_search([succ[v,c] | v in VEHICLES,c in CUSTOMERS],smallest,indomain_max,complete) minimize distanceTravelled;
    """
)
####################################################

# initialise the parameters in the minizinc
instance = Instance(gecode, problem)
instance['n'] = num_cust-1
instance['m'] = max_num_vehicles
instance['capacity'] = max_vehicle_capacity
instance['demand'] = demands
# instance['service'] = [90,90,90,90,90,0]
# instance['ready_time'] = [912,825,65,727,15,0]
# instance['due_time'] = [967,870,146,782,67,1236]
instance['distance'] = dist

result = instance.solve()

vehicles_used = result['vehiclesUsed']
# print(np.array(result['succ'])[:vehicles_used])
print('#'*10 + ' SOLUTION FOUND ' + '#'*20)
print(f'Distance Travelled: {result["distanceTravelled"]}')
print(f'Number of Vehicles used: {result["vehiclesUsed"]}')
print('#'*50)
paths = np.array(result['succ'])[:vehicles_used]

# plot the graph
G = nx.DiGraph() 
G.add_nodes_from(node_names)

# add colours to the paths depending on which vehicle visits it
for vehicle_num in range(paths.shape[0]):
    for dest_num in range(paths.shape[1]):
        G.add_edge(dest_num+1,paths[vehicle_num,dest_num],weight=dist[dest_num][paths[vehicle_num,dest_num]-1], color=colors[vehicle_num])

edgelist = G.edges()
nodelist = G.nodes()
edge_colors = [G[u][v]['color'] for u,v in edgelist]
edge_labels = nx.get_edge_attributes(G,'weight')
############################################################
# nx.draw(G,pos=pos,with_labels=True, node_colors='light_blue', edge_colors=edge_colors,connectionstyle='arc3, rad = 0.1')
# nx.draw_networkx_edge_labels(G,pos=pos,edge_labels=labels)
############################################################
nx.draw_networkx_nodes(G,pos,with_labels=True,nodelist=nodelist,node_color='b')
nx.draw_networkx_labels(G, pos, node_labels)
nx.draw_networkx_edges(G,pos,edgelist=edgelist,edge_color=edge_colors,connectionstyle='arc3, rad = 0.1')
nx.draw_networkx_edge_labels(G,pos=pos,edge_labels=edge_labels)
plt.title('Path found by the solver')
plt.show()
############################################################