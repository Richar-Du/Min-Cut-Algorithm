import networkx as nx
import heapq
import numpy as np

def MyStoerWagner(Graph):
    # 输入：用networkx表示的图Graph
    # 输出：全局最小割及其值
    vertex_num=len(Graph)           # 点的数量
    cut_value = float('inf')        #  最小割值初始化为无穷大
    nodes = set(Graph)              # 点集
    contractions = []               # 记录每次收缩的点
    InitialPNT=Graph.nodes()[np.random.randint(0,vertex_num)]     # 随机选一个初始点加入到A中
    print(InitialPNT)
    for i in range(vertex_num-1):               # 直到除了A之外只有一个点
        A = {InitialPNT}
        h = []  # h用来记录A中点的邻接点
        for vertex, attribute in Graph[InitialPNT].items():
            heapq.heappush(h,[-attribute['weight'],vertex])          # vertex是和u相邻的点，weight是权重，因此h存的是初始点的所有邻接点
        for j in range(vertex_num-i-2):         # 每次收缩一个点，因此往A中加的点就少一个
            print('h=',h)
            most_tighted_v = heapq.heappop(h)[1]                # most_tighted_v是离初始点权重最大的点
            print("most tighted is ",most_tighted_v)
            # most_tighted_v=h.pop(min(h))          # 因为h是堆，因此直接pop就可以弹出最小值，即权重最大值，most_tighted_v是离初始点权重最大的点
            A.add(most_tighted_v)
            print("after adding, now A is:",A)
            for v, e, in Graph[most_tighted_v].items():          # u是刚加入A的点，如果它的邻接点v不在A中，就加到h中去
                if v not in A:
                    index=get_heap_element(h,v)
                    if index!=-1:
                        h[index][0]-=e['weight']            # 如果v已经在h中了，就把权重累加
                        heapq.heapify(h)
                    else:
                        heapq.heappush(h, [-e['weight'],v])           # 如果v不在h中，就新建一个
        print("看看last的时候h中是不是只有一个点，h=",h)
        last, w = h[0][1],h[0][0]  # 上面的for循环结束之后只剩下一个点v不在A中了，它是最后一个点也是h中唯一的点
        w=-w
        print("phase=",i,'min cut value=',w)
        if w < cut_value:
            cut_value = w
            best_phase = i
        # Contract v and the last node added to A.
        contractions.append((most_tighted_v, last))
        print("contractions=",contractions)
        for w, e in Graph[last].items():  # 遍历last的所有邻接点
            if w != most_tighted_v:
                if w not in Graph[most_tighted_v]:  # 如果v的邻接点不和u相邻，就让他们相邻
                    Graph.add_edge(most_tighted_v, w, weight=e['weight'])
                else:
                    Graph[most_tighted_v][w]['weight'] += e['weight']  # 如果v的邻接点和u相邻，权重相加
        Graph.remove_node(last)  # 把v删掉
        # print("removed:",last)
    partition=[]
    for i in range(best_phase):
        for j in contractions[i]:
            if j not in partition:
                partition.append(j)
    partition=(set(partition),nodes-set(partition))
    # G = nx.Graph(islice(contractions, best_phase))
    # v = contractions[best_phase][1]
    # G.add_node(v)
    # reachable = set(nx.single_source_shortest_path_length(G, v))
    # partition = (list(reachable), list(nodes - reachable))
    return cut_value,partition

def get_heap_element(HEAP,vertex):
    vertex_name_list=[]
    for i in HEAP:
        vertex_name_list.append(i[1])
    if vertex in vertex_name_list:
        index=vertex_name_list.index(vertex)
        return index
    else:
        return -1

# RodeEU_gcc=np.loadtxt('data/RodeEU_gcc.txt',dtype=int)
# RodeEU_gcc_Graph=nx.Graph()
# for line in RodeEU_gcc:
#     RodeEU_gcc_Graph.add_edge(int(line[0]),int(line[1]),{'weight':1})
#
# cut_value= MyStoerWagner(RodeEU_gcc_Graph)
# print('cut_value=',cut_value)


G = nx.Graph()
G.add_edge('x','a', weight=3)
G.add_edge('x','b', weight=1)
G.add_edge('a','c', weight=3)
G.add_edge('b','c', weight=5)
G.add_edge('b','d', weight=4)
G.add_edge('d','e', weight=2)
G.add_edge('c','y', weight=2)
G.add_edge('e','y', weight=3)
cut_value,cut=MyStoerWagner(G)
print('cut_value=',cut_value,'cut=',cut)


