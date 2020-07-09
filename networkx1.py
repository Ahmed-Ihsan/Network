# Ahmed Ihsan Ali
import networkx as nx
import matplotlib.pyplot as plt
row = [(1,1),(2,2),(3,0),(4,2),(5,0),(6,2)] 
row2=[0,0,0,0,0,0]
row3=[0,0,0,0,0,0]
row4=[0,0,0,0,0,0]
row5=['A','B','C','D','E','F']
row6=[0,0,0,0,0,0]
num=0
add=0
n2=1000

for item in row:
	add=0
	for item2 in item:
		add=item2+add
	row2[num]=add
	num=num+1
add2=0
#print(row2)             
#[2, 4, 3, 6, 5, 8]
#===========================================================================================
for i in row2:
	add=0
	for item in row2:
		n=i-item
		if n < 0:
		  n=n*-1
		if True:
			row4[add]=n
			add=add+1
	#print(row4)
	#======================================================================================
	
	index=0
	for item in row4:
		for j in row4:
			if item < j :
				if n2 > item and item !=0 :
				 n2=item
				 #print(n2)
				 row6[add2]=n2
				 row3[add2]=index
		#print(row6)
		index=index+1
	#print(row3)
	
	add2=add2+1
	n2=1000

#==========================================================================================

G=nx.Graph()

G.add_edge(row5[0],row5[row3[1]],weight=row6[0])
G.add_edge(row5[1],row5[row3[2]],weight=row6[1])
G.add_edge(row5[2],row5[row3[3]],weight=row6[2])
G.add_edge(row5[3],row5[row3[4]],weight=row6[3])
G.add_edge(row5[4],row5[row3[5]],weight=row6[4])
G.add_edge(row5[5],row5[row3[0]],weight=row6[5])

pos =nx.spring_layout(G)

nx.draw(G,pos,with_labels=True)
nx.draw_networkx_edge_labels(G,pos,with_labels=True,font_size=10,edge_labels=nx.get_edge_attributes(G,'weight'))
plt.show() # display