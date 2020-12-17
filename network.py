import networkx as nx
import pydot
import graphviz
import os

#//////////////////////////////////////////////////////////////////////////////////////////////#

def drawLine(ToNode , shortest_path ,Color):
	x=1
	for i in ToNode:
		if x != 1:
			M.add_edge(shortest_path[i][-1],shortest_path[i][-2],color=Color)
		x=0

def cost(node1 , node2 , capacity , weight):
	MCMF=nx.max_flow_min_cost(G, node1 ,node2, capacity= capacity ,weight= weight )
	MCMF=nx.cost_of_flow(G,MCMF)
	print(f'cost from {node1} to {node2} = {MCMF}')

#//////////////////////////////////////////////////////////////////////////////////////////////#

G=nx.DiGraph()
h=graphviz.Graph()

h.engine='neato'
G.add_node('A',pos="0,1!" )
G.add_node('B',pos="0,-1!")
G.add_node('C',pos="2,1!" )
G.add_node('D',pos="2,-1!")
G.add_node('E',pos="4,1!" )
G.add_node('F',pos="4,-1!")
G.add_node('G',pos="6,0!" )

G.add_edge('A','D',weight=10,capacity=15,label='10;15')
G.add_edge('A','C',weight=5,capacity=4,label='5;4')
G.add_edge('B','D',weight=5,capacity=10,label='5;10')
G.add_edge('B','C',weight=7,capacity=8,label='7;8')
G.add_edge('C','E',weight=3,capacity=17,label='3;17')
G.add_edge('C','F',weight=3,capacity=4,label='3;4')
G.add_edge('D','C',weight=1,capacity=4,label='1;4')
G.add_edge('D','E',weight=5,capacity=6,label='5;6')
G.add_edge('D','F',weight=8,capacity=8,label='8;8')
G.add_edge('E','G',weight=1,capacity=14,label='1;14')
G.add_edge('G','F',weight=2,capacity=5,label='2;5')

#//////////////////////////////////////////////////////////////////////////////////////////////#

p = nx.shortest_path(G, source='B', weight='weight')
p2 = nx.shortest_path(G, source='A', weight='weight')

print(p2['F'])

M=nx.MultiDiGraph(G)

drawLine(p['E'] , p ,'red')
drawLine(p2['F'] , p2 ,'blue')

cost('A','F','capacity','weight')
cost('B','E','capacity','weight')

#//////////////////////////////////////////////////////////////////////////////////////////////#

filename = "nx_sp"
nx.drawing.nx_pydot.write_dot(M, filename + ".dot")

# in windows graphviz 
# run neato by dot -Kneato
os.system("dot -Kneato -T png "+ filename + ".dot -o " + filename + ".png")
#os.system("dot -T png " + filename + ".dot -o " + filename + ".png")

