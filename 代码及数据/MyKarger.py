from random import randint
from math import log
import numpy as np
import math
import copy
class Karger():
    ##数据处理工作，将图初始化成字典的形式
    def __init__(self,graph_file):
        self.graph={}
        self.vertex_count=0
        self.edges=0
        self.over_poind = {}
        my_data = np.loadtxt(graph_file, dtype="int")
        lie_1 = my_data[:, 0]
        lie_2 = my_data[:, 1]
        unique_data = np.unique(my_data)
        for i in range(1, len(unique_data) + 1):
            self.graph[i] = []
            for num in range(0, len(lie_1)):
                if lie_1[num] == i:
                    self.graph[i].append(lie_2[num])
            for num2 in range(0, len(lie_2)):
                if lie_2[num2] == i:
                    if lie_1[num2] not in self.graph[i]:
                        self.graph[i].append(lie_1[num2])
        for i in range(1,len(self.graph)+1):
            self.vertex_count+=1
            self.edges+=len(self.graph[i])
            self.over_poind[i] = [i]###supervertices用来存储最后合并的结果
    #这里开始寻找最小割的函数
    def search_min_cut(self):
        minimumcut = 0##让他初始化等于0
        while len(self.graph)>2:
            #print("这一次循环的变化情况")
            #print(self.supervertices)
            # 先选择一条随机的边，同时得到随机的点
            vertice1, vertice2 = self.random_select()
            self.edges -= len(self.graph[vertice1])###边数应该减掉和这两个点相通的所有点长度的和，即在边集合中删除这俩
            self.edges -= len(self.graph[vertice2])
            # 然后合并这个图
            self.graph[vertice1].extend(self.graph[vertice2])###图的数据集中把vertice2相关的点加到vertice1里面去
            # Update every references from v2 to point to v1
            for vertex in self.graph[vertice2]:
                self.graph[vertex].remove(vertice2)
                self.graph[vertex].append(vertice1)
            # 删除自环！！！！！！
            self.graph[vertice1] = [x for x in self.graph[vertice1] if x != vertice1]
            # 更新图的全部的边
            self.edges += len(self.graph[vertice1])###再加上合并之后的值
            self.graph.pop(vertice2)###图的集合中彻底删除vertice2的数据
            # 更新图的割集
            self.over_poind[vertice1].extend(self.over_poind.pop(vertice2))
            ###循环之后图中就剩两个点，这两个点中间的连线就是最小割
        #然后现在可以来计算最小割了
        for edges in self.graph.values():
            minimumcut = len(edges)
        #  最后返回最小割和形成的两个集合
        return minimumcut,self.over_poind
    # 选取随机边的函数
    def random_select(self):
        rand_edge = randint(0, self.edges-1)###生成一个随机的值，从0到所有边数中
        for key, value in self.graph.items():
            if len(value) < rand_edge:###从第一行开始逐渐寻找那条边，第一行不是就减掉第一行的长度，知道该行长度超过了边数
                rand_edge -= len(value)
            else:
                vertex_origin = key
                vertex_last = value[rand_edge-1]
                return vertex_origin, vertex_last   ##返回索引点和索引点集合里的点
if __name__ == '__main__':
    minimumcut=9999###只是一个足够大的值用来比较最小割
    graph_feature = Karger('data/RodeEU_gcc.txt')
    iterations = len(graph_feature.graph) * len(graph_feature.graph) * int(math.log(len(graph_feature.graph)))  #运算次数
    print("一共需要运行{}次".format(iterations))
    for i in range(10):
        graph_copy =Karger('data/RodeEU_gcc.txt')
        result = graph_copy.search_min_cut()
        #if result[0]==1:###任何一次找到最小割为1都可以停止循环，因为最小为1.
           # minimumcut = result[0]
            #over_point = result[1]
            ##break
        #else:
        if result[0] < minimumcut:
            minimumcut = result[0]
            over_point = result[1]
    print("最小割的值是:{}".format(minimumcut))
    for key in over_point:
        print("源点是{}，集合内的元素为{}".format(key, over_point[key]))