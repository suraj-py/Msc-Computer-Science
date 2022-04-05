
# Practical 2

# Perform following tasks: 
# (i) View data collection forms and/or import onemode/two-mode datasets; 

nodes <- read.csv("CSV Files/nodes.csv")
head(nodes)

links <- read.csv("CSV Files/edges.csv")
head(links)

# (ii) Basic Networks matrices transformations

library(igraph)
net <- graph.data.frame(d=links, vertices=nodes, directed=T)
m=as.matrix(net)
get.adjacency(m)

plot(net)
