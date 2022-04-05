
# Practical 6

# Write a program to exhibit structural equivalence, automatic equivalence,
# and regular equivalence from a network.
print(getwd())
library(sna)

library(igraph)

links2 <- read.csv("CSV Files/edges1.csv", header=T, row.names=1)

eq<-equiv.clust(links2)

plot(eq)

g.se<-sedist(links2)

plot(cmdscale(as.dist(g.se)))
b<-blockmodel(links2,eq,h=10)
plot(b)

