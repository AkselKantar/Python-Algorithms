graph = {
  "A" : ["B","C"],
  "B" : ["D", "E"],
  "C" : ["F"],
  "D" : [],
  "E" : ["F"],
  "F" : []
}

visited = []
queue = []

def breadth_first_search(visited, graph, node):
   visited.append(node)
   queue.append(node)

   while queue:
       m = queue.pop(0)
       print(m)

       for neighbour in graph[m]:
           if neighbour not in visited:
               visited.append(neighbour)
               queue.append(neighbour) 


#############################################

breadth_first_search(visited, graph, "A")


