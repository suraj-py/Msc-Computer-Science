
#Practical 1
#Write a program to compute the following for a given a network: 
#(i) number of edges, 
#(ii)number of nodes, 
#(iii) degree of node, 
#(iv) node with lowest degree, 
#(v) the adjacency list,
#(vi) matrix of the graph.

# import igraph lib
library(igraph)

# Graph 1
ug <- graph.formula(A-B,A-C,A-D,B-C,B-D,B-E,C-E,D-F,E-F)
plot(ug)

ecount(ug)
vcount(ug)

E(ug)
V(ug)

degree(ug)
V(ug)$name[degree(ug)==max(degree(ug))]

get.adjacency(ug) 
get.adjlist(ug)

# Graph 2
dg <- graph.formula(A-+B, A+-B, A++C, B-+C, C-+D, D++A, D-+B, E-+C)
plot(dg)

degree(dg,mode="in")
degree(dg,mode="out")
degree(dg)

V(dg)$name[degree(dg,mode="in")==min(degree(dg,mode = "in"))]

