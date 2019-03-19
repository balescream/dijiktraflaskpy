import sys
from flask import Flask, request,render_template
app=Flask(__name__) 
f=open("db.txt","r")  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                      for row in range(vertices)] 

    def minDistance(self, dist, sptSet): 
  
        # Initilaize minimum distance for next node 
        min = sys.maxsize
        min_index=0
        # Search not nearest vertex not in the  
        # shortest path tree 
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
        return min_index 
  
 
    # using adjacency matrix representation 
    def dijkstra(self, src): 
        parent=[None]*self.V
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        parent[src]=-1 
        for cout in range(self.V): 
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.minDistance(dist, sptSet) 
  
            # Put the minimum distance vertex in the  
            # shortest path tree 
            sptSet[u] = True
            # Update dist value of the adjacent vertices  
      
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                        dist[v] = dist[u] + self.graph[u][v] 
                        parent[v]=u;  
  
        
        return parent
  
# Driver program
@app.route('/',methods=['POST','GET'])
def homepage():
    return render_template('input.html') 
g  = Graph(51)
for x in f:
  t=x.split("\t")
  g.graph[int(t[0])][int(t[1])]=int(t[2])
@app.route('/result',methods=['POST','GET'])
def result():
  if request.method=='POST':
   # if not result['source']|| not result['dest']:
      
    parent=g.dijkstra(int(request.form['source']))
    l=[None]

    l.append(request.form['dest'])
    i=request.form['dest']
    i=int(i)
    while not parent[i]==-1:
      l.append(parent[i])
      i=parent[i] 
    l.reverse()
    l.pop()

  return render_template("index.html",l=l)

if __name__=='__main__':
  app.run(debug=True, port=5000)  
 