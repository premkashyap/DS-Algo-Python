from typing import Dict, List, Tuple

class UndirectionalGraph:
    
    def __init__(self):
        self.gdict = {}
    #Add the new edge
    def setEdge(self, edge: Tuple):
        (vrtx1, vrtx2) = edge
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]
        
        if vrtx2 in self.gdict:
            self.gdict[vrtx2].append(vrtx1)
        else:
            self.gdict[vrtx2] = [vrtx1]

    def addVertex(self, vrtx):
        if type(vrtx) is not list:
            self.gdict[vrtx] = []
        else:
            for vertex in vrtx:
                self.gdict[vertex] = []
    #List the edge names
    def printEdges(self) -> None:
        for vrtx in self.gdict.keys():
            print(vrtx + ':', end='\t')
            print(self.gdict[vrtx])

    def hasEdge(self, edge):
        (a,b) = edge
        try:
            return b in self.gdict[a]
        except KeyError:
            return False
    
    def BFS(self, vrtx=None):
        def _BFS(vrtx):
            if vrtx not in self.gdict.keys():
                return 
            queue = [vrtx]
            vertices = []
            for item in self.gdict.keys():
                while queue:
                    vrtx = queue.pop(0)
                    if vrtx not in vertices:
                        vertices.append(vrtx)
                    for vertex in self.gdict[vrtx]:
                        if vertex is not None and vertex not in vertices:
                            queue.append(vertex)
            return vertices
        if vrtx is not None:
            return _BFS(vrtx)
        else:
            paths = []
            for item in self.gdict.keys():
               for path in paths:
                   if item in path:
                       continue
               v = _BFS(item)
               paths.append(v)
            return paths
    
    def DFS(self, vrtx = None):
        def _DFS(vrtx):
            if vrtx not in self.gdict.keys():
                return 
            stack = [vrtx]
            vertices = []
            for item in self.gdict.keys():
                while stack:
                    vrtx = stack.pop()
                    if vrtx not in vertices:
                        vertices.append(vrtx)
                    for vertex in self.gdict[vrtx]:
                        if vertex is not None and vertex not in vertices:
                            stack.append(vertex)
            return vertices
        if vrtx is not None:
            return _DFS(vrtx)
        else:
            vertices = []
            for item in self.gdict.keys():
                v =_DFS(item)
                for item in v:
                    if item not in vertices:
                        vertices.append(item)
            return vertices


        
class DirectedGraph:
    def __init__(self):
        self.graph = {}
    
    def setEdge(self, edge: Tuple):
        self.graph[edge[0]].append(edge[1])

    def hasEdge(self, edge: Tuple):
        try:
            return edge[1] in self.graph[edge[0]]
        except KeyError:
            return False
    
    def addVertex(self, a):
        self.graph[a] = []

    def BFS(self, vrtx = None):
        def _BFS(vrtx):
            if vrtx not in self.graph.keys():
                return 
            queue = []
            vertices = []
            queue.append(vrtx)
            while queue:
                vertex = queue.pop(0)
                if vertex not in vertices:
                    vertices.append(vertex)
                for v in self.graph[vertex]:
                    if v is not None:
                        queue.append(v)
        
        if vrtx is not None:
            return _BFS(vrtx)
        else:
            paths = []
            for vertex in self.graph.keys():
                for path in paths:
                    if vertex in path:
                        continue
                path = _BFS(vertex)
                paths.append(path)
            return paths
                
    def DFS(self, vrtx = None):
        def _DFS(vrtx):
            if vrtx not in self.graph.keys():
                return 
            stack = []
            vertices = []
            stack.append(vrtx)
            while stack:
                vertex = stack.pop()
                if vertex not in vertices:
                    vertices.append(vertex)
                for v in self.graph[vertex]:
                    if v is not None:
                        stack.append(v)
    
        if vrtx is not None:
            return _DFS(vrtx)
        else:
            paths = []
            for vertex in self.graph.keys():
                for path in paths:
                    if vertex in path:
                        continue
                path = _DFS(vertex)
                paths.append(path)
            return paths






        

if __name__ == '__main__':
    g = UndirectionalGraph()
    g.addVertex(['a','b','c','d','e'])
    g.setEdge(('a', 'd'))
    g.setEdge(('a', 'e'))
    g.setEdge(('d', 'b'))
    g.setEdge(('e', 'c'))
    g.printEdges()
    print(g.BFS('a'))
    print(g.DFS('a'))
    print(g.hasEdge(('e', 'a')))
