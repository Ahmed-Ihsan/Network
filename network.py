import networkx as nx
import pydot
import graphviz
import os

G=nx.DiGraph()
h=graphviz.Graph()

h.engine='neato'
G.add_node('A',pos="0,1!" )
G.add_node('B',pos="0,-1!" )
G.add_node('C',pos="2,1!" )
G.add_node('D',pos="2,-1!" )
G.add_node('E',pos="4,1!" )
G.add_node('F',pos="4,-1!" )
G.add_node('G',pos="6,0!" )

pos_node=[5.4,10.15,5.10,7.8,3.17,3.4,1.4,5.6,8.8,1.14,2.5]

G.add_edge('A','D',weigth=pos_node[0],label=f'w:{pos_node[0]}')
G.add_edge('A','C',weigth=pos_node[1],label=f'w:{pos_node[1]}')
G.add_edge('B','D',weigth=pos_node[2],label=f'w:{pos_node[2]}')
G.add_edge('B','C',weigth=pos_node[3],label=f'w:{pos_node[3]}')
G.add_edge('C','E',weigth=pos_node[4],label=f'w:{pos_node[4]}')
G.add_edge('C','F',weigth=pos_node[5],label=f'w:{pos_node[5]}')
G.add_edge('D','C',weigth=pos_node[6],label=f'w:{pos_node[6]}')
G.add_edge('D','E',weigth=pos_node[7],label=f'w:{pos_node[7]}')
G.add_edge('D','F',weigth=pos_node[8],label=f'w:{pos_node[8]}')
G.add_edge('E','G',weigth=pos_node[9],label=f'w:{pos_node[9]}')
G.add_edge('G','F',weigth=pos_node[10],label=f'w:{pos_node[10]}')

p = nx.shortest_path(G, source='B', weight='weight')

print(p['D'])
print(p['E'])

M=nx.MultiDiGraph(G)

M.add_edge(p['D'][-1],p['D'][-2],color='red')
M.add_edge(p['E'][-1],p['E'][-2],color='red')

filename = "nx_sp"
nx.drawing.nx_pydot.write_dot(M, filename + ".dot")

# in windows graphviz 
# run neato by dot -Kneato
os.system("dot -Kneato -T png "+ filename + ".dot -o " + filename + ".png")
# or dot by dot only
#os.system("dot -T png " + filename + ".dot -o " + filename + ".png")



