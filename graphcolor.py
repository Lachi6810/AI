node=input("Enter the nodes without spaces: ")
G=[]
print("Enter the edges with 0's and 1's: ")
for i in range(len(node)):
  l=[]
  l=list(map(int,input(" ").split()))
  G.append(l)
t_={}
for i in range(len(G)):
  t_[node[i]] = i
degree=[]
for i in range(len(G)):
  degree.append(sum(G[i]))
colorDict={}
for i in range(len(G)):
  colorDict[node[i]]=["Blue","Red","Yellow","Green"]
sortedNode=[]
indeks = []
for i in range(len(degree)):
  _max = 0
  j = 0
  for j in range(len(degree)):
    if j not in indeks:
      if degree[j] > _max:
        _max = degree[j]
        idx = j
  indeks.append(idx)
  sortedNode.append(node[idx])
theSolution={}
for n in sortedNode:
  setTheColor = colorDict[n]
  theSolution[n] = setTheColor[0]
  adjacentNode = G[t_[n]]
  for j in range(len(adjacentNode)):
    if adjacentNode[j]==1 and (setTheColor[0] in colorDict[node[j]]):
      colorDict[node[j]].remove(setTheColor[0])
for t,w in sorted(theSolution.items()):
  print("Node",t," = ",w)
