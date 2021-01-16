import networkx as nx
import numpy as np
BenchmarkNetwork=np.loadtxt('data/BenchmarkNetwork.txt',dtype=int)
Corruption_Gcc=np.loadtxt('data/Corruption_Gcc.txt',dtype=int)
Crime_Gcc=np.loadtxt('data/Crime_Gcc.txt',dtype=int)
PPI_gcc=np.loadtxt('data/PPI_gcc.txt',dtype=int)
RodeEU_gcc=np.loadtxt('data/RodeEU_gcc.txt',dtype=int)
# 用Networkx
BenchmarkNetwork_Graph=nx.Graph()
for line in BenchmarkNetwork:
    BenchmarkNetwork_Graph.add_edge(int(line[0]),int(line[1]),{'weight':1})
cut_value, partition = nx.stoer_wagner(BenchmarkNetwork_Graph)
print("BenchmarkNetwork的最小割是：",cut_value,partition)

RodeEU_gcc_Graph=nx.Graph()
for line in RodeEU_gcc:
    RodeEU_gcc_Graph.add_edge(int(line[0]),int(line[1]),{'weight':1})
cut_value, partition = nx.stoer_wagner(RodeEU_gcc_Graph)
print("RodeEU_gcc的最小割是：",cut_value,partition)

Corruption_Gcc_Graph=nx.Graph()
for line in Corruption_Gcc:
    Corruption_Gcc_Graph.add_edge(int(line[0]),int(line[1]),{'weight':1})
cut_value, partition = nx.stoer_wagner(Corruption_Gcc_Graph)
print("Corruption_Gcc的最小割是：",cut_value,partition)

Crime_Gcc_Graph=nx.Graph()
for line in Crime_Gcc:
    Crime_Gcc_Graph.add_edge(int(line[0]),int(line[1]),{'weight':1})
cut_value, partition = nx.stoer_wagner(Crime_Gcc_Graph)
print("Crime_Gcc的最小割是：",cut_value,partition)

PPI_gcc_Graph=nx.Graph()
for line in PPI_gcc:
    PPI_gcc_Graph.add_edge(int(line[0]),int(line[1]),{'weight':1})
cut_value, partition = nx.stoer_wagner(PPI_gcc_Graph)
print("PPI_gcc的最小割是：",cut_value,partition)
