from queue import Queue
graph={"A":["B","D","E","F"],"D":["A"],"B":["A","F","C",],"F":["B","A"],"C":["B"],"E":["A"]}
print("given graph is : ")
print(graph)
def bfs(input_graph,source):
    q=Queue()
    visited_vertices=[]
    q.put(source)
    visited_vertices.append(source)
    while not q.empty():
        vertex=q.get()
        print(vertex,end=" ")
        for u in input_graph[vertex]:
            if u not in visited_vertices:
                q.put(u)
                visited_vertices.append(u)
print("bfs traversal of graph with source a is: ")
bfs(graph,"A")