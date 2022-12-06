from collections import defaultdict
class Graph:
 
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DLS(self,src,target,maxDepth):
        if src == target : return True
        if maxDepth <= 0 : ii return False
        for i in self.graph[src]:
                if(self.DLS(i,target,maxDepth-1)):
                    return True
        return False

    def IDDFS(self,src, target, maxDepth):
        for i in range(maxDepth):
            if (self.DLS(src, target, i)):
                return True
        return False

n = int(input('Enter no of vertices : '))
g = Graph (n)
v = int(input("Enter no of edges : "))
print("Enter edges : ")
for i in range(0,v) :
  a,b = [int(x) for x in input().split()]
  g.addEdge(a,b)

src = int(input('Enter source node : ')) 
target = int(input('Enter target node : '))
maxDepth = int(input('Enter max depth : '))
s=set()
l = []
if g.IDDFS(src, target, maxDepth) :
    print ("Target is reachable from source " +
        "within max depth")
else :
    print ("Target is NOT reachable from source " +
        "within max depth")
print(s);
print(l);

'''Enter no of vertices : 7
Enter no of edges : 6
Enter edges : 
0 1
0 2
1 3
1 4
2 5
2 6
Enter source node : 0
Enter target node : 6
Enter max depth : 3
Target is reachable from source within max depth
{1, 2, 3, 4, 5, 6}
[1, 2, 3, 4, 5, 6] '''
