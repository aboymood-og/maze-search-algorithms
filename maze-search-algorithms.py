#Enfoque (Approach)
#Empieza con una frontier que contiene el estado inicial.
#Repetir:
#   • Si la frontera es vacía, entonces no hay solución.
#   • Borrar un nodo de la frontera.
#   • Si el nodo contiene el estado objetivo, return la solución.
#   • Expandir nodo, agregar nodos resultantes a la frontera.

#Definir laberito y punto de partida (s) y goal (g)
#Llegar desde s a g
maze = [["s"," "," ","g"],
        ["X"," ","X","X"],
        ["X"," ","X","X"],
        ["X","X","X","X"]]

def find_start_goal(maze):
  for y in range(len(maze)):
    for x in range(len(maze[y])):
      if maze[y][x] == "s":
        start = (y,x)
      elif maze[y][x] == "g":
        goal = (y,x)
        return start, goal

def find_frontiers(agent):
  
  posible_frontiers = [(agent[0], agent[1] - 1), #izquierda
                       (agent[0] - 1, agent[1]), #arriba
                       (agent[0], agent[1] + 1),     #derecha
                       (agent[0] + 1, agent[1])]     #abajo


  i = 0 
  while i != len(posible_frontiers):
    if (posible_frontiers[i][0] or posible_frontiers[i][1]) < 0:
      posible_frontiers.pop(i)
    elif maze[posible_frontiers[i][0]][posible_frontiers[i][1]] == "X":
      posible_frontiers.pop(i)
    elif posible_frontiers[i] in path:
      posible_frontiers.pop(i)
    else:
      i += 1
  return posible_frontiers

start, goal = find_start_goal(maze)
print("Punto de inicio:", start, "\nPunto de meta: \t", goal)

#Empieza con una frontier que contiene el estado inicial
frontier = []
frontier.append(start)  
print("Frontier:", frontier)

#Repetir
path = []
agent = None
while agent != goal:
  path.append(agent)
  print("Path: ", path)
  #Si la frontera es vacía, entonces no hay solución
  if len(frontier) == 0:
    print("No hay solución")
    break
  #Borrar un nodo de la frontera
  agent = frontier.pop(0)
  print("Agente:", agent)

  if agent == goal:
    print("\n¡Meta alcanzada!")
    print("Camino recorrido: ", path)
    break
    
    
  
  #Expandir nodo, agregar nodos resultantes a la frontera
  frontier = find_frontiers(agent)
  print("frontier: ", frontier)
  