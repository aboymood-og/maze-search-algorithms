#--------------------------- FUNCIONES ---------------------------#
#funcion para encontrar "s" y "g" en el laberinto
def find_start_goal(maze):
  start = None  #se inicializa cada variable a buscar
  goal = None
  for col in range(len(maze)): #Se recorre todo el laberinto buscando "s" y "g"
    for row in range(len(maze[col])): 
      if maze[col][row] == "s":
        start = (col,row)
      elif maze[col][row] == "g":
        goal = (col,row)
      if start != None and goal != None: #verifica dentro de cada iteración si se encontro "s" y "g"
        return start, goal
  if start == None or goal == None: #si no se encontro "s" y "g" se usa esta funcion que devuelve un error y termina todo el programa
    return start, goal
    
#funcion para encontrar posibles fronters, es decir, que no salgan del limite del laberinto, que no sean paredes/limites, y que no hallan sido recorridas antes
def find_frontiers(agent):
  #se crea una lista que añade todas las posibles fronteras, es decir, los 4 lados que limitan la posición actual del agente
  posible_frontiers = [(agent[0], agent[1] - 1),     #izquierda
                       (agent[0] - 1, agent[1]),     #arriba
                       (agent[0], agent[1] + 1),     #derecha
                       (agent[0] + 1, agent[1])]     #abajo
  #bucle para verificar que las posibles fronteras cumplan ciertas condiciones, de lo contrario se eliminan de la lista "posible_frontiers"
  i = 0 
  while i != len(posible_frontiers): 
    if posible_frontiers is []: #verifica si hay posibles frontiers, en caso de que no y la lista este vacia, retorna la lista vacia 
      return posible_frontiers
    elif posible_frontiers[i][0] >= len(maze) or posible_frontiers[i][1] >= len(maze[0]): #verifica que la posible frontera no salga del margen del laberinto, si sale se elimina de "posible_frontiers"
      posible_frontiers.pop(i) 
    elif posible_frontiers[i][0]  < 0 or posible_frontiers[i][1] < 0: #verifica que la posible frontera no sea negativa, si es negativa la elimina de "posible_frontiers"
      posible_frontiers.pop(i)
    elif maze[posible_frontiers[i][0]][posible_frontiers[i][1]] == "X": #verifica que la posible frontera no sea una pared/limite, si es una pared o limite la elmina de "posible_frontiers"
      posible_frontiers.pop(i)
    elif posible_frontiers[i] in explored_set: #verifica que la posible frontera no halla sido recorrido previamente por el agente, si lo fué la elimina de "posible_frontiers"
      posible_frontiers.pop(i)
    else: #en caso de que no cumpla ninguna condicion anterior, es valida para ser frontera por lo que se mantiene y aumenta la iteración para seguir con el siguiente elemento de la lista "posible_frontiers"
      i += 1
  for i in range(len(posible_frontiers)): #una vez tenemos la lista de fronteras se guardan en el diccionario, guardando la frontera -> nodo padre (agente en este caso)
      shortest_path[posible_frontiers[i]] = agent
  return posible_frontiers #una vez se verifican las 4 posibles fronteras y no tenemos lista vacia, retorna la lista con las fronteras definitivas para el agente

#funcion para imprimir el laberinto en pantalla
def print_maze(maze):
  for fila in maze:
    print(' '.join(fila))

#funcion para elegir algoritmo de busqueda
def choose_algorithm():    
  while True:
    aux = input("Eliga que algoritmo usar: \n (1): BFS (cola) \n (2): DFS (pila) \n (3): Greddy Best First with Manhattan Heuristic \n\nEscriba 1, 2 o 3:")
    if aux == "1":
      print("\nSolución con BFS:")
      alg = 0
      return alg
    elif aux == "2":
      print("\nSolución con DFS:")
      alg = -1
      return alg
    elif aux == "3":
      print("\nSolución con Greddy Best First with Manhattan Heuristic")
      alg = 3
      return alg
    else:
      print("Debe elegir entre [1,2,3]. Intentar denuevo.\n")

#funcion para buscar el camino mas corto usando diccionarios
def find_shortest_path(shortest_path):
  path_shorter = []
  vecino = goal
  while vecino != start:
    path_shorter.append(vecino)
    vecino = shortest_path[vecino]
  path_shorter.append(start)
  path_shorter = path_shorter[::-1]
  return path_shorter

#funcion que dibuja el laberito con el camino mas corto
def draw_shortest_path(maze, sp):
  for col in range(len(maze)): #Se recorre todo el laberinto buscando "s" y "g"
    for row in range(len(maze[col])): 
      if (col,row) in sp and maze[col][row] != "s" and maze[col][row] != "g":
        maze[col][row] = "·"
  return maze

#funcion para aplicar manhatann
def manhatann(frontier):
  frontier2 = frontier.copy()
  for f in range(len(frontier2)):
    d = abs(frontier2[f][0]-goal[0]) + abs(frontier2[f][1]-goal[1])
    frontier2[f] = d
  #print("agentemanhattan:", agent)
  #print("frontiermanhatan:", frontier)
  #print("frontier2manhata:", frontier2)
  #print("minfrontier:", frontier2.index(min(frontier2)))

  alg = frontier2.index(min(frontier2))
  return alg

#--------------------------- FUNCIONES ---------------------------# 

#---------------------- PROGRAMA PRINCIPAL -----------------------# 
#inicializar laberinto
#maze = [["X"," "," "," ","X","X","X","X"],  # X = paredes/limites3
#        ["X"," ","X"," "," "," ","X","X"],  # s = punto de inicio
#        ["X","s","X"," ","X"," "," ","g"],  # g = punto de meta
#        ["X","X","X"," "," "," ","X","X"]]
  
maze = [
  ["X","X","X","X","X","X","X","X","X","X","X","X","X","X"],
  ["X","s"," "," "," "," "," "," "," ","X"," "," "," ","X"],
  ["X"," ","X"," ","X"," ","X","X"," ","X"," ","X"," ","X"],
  ["X"," ","X"," ","X"," "," ","X"," "," "," ","X"," ","X"],
  ["X"," ","X","X","X","X"," ","X","X","X"," ","X"," ","X"],
  ["X"," "," "," "," ","X"," "," "," ","X"," "," "," ","X"],
  ["X","X","X","X"," ","X","X","X"," ","X","X","X"," ","X"],
  ["X"," "," "," "," "," "," ","X"," "," "," "," "," ","X"],
  ["X"," ","X","X","X","X","X","X","X","X","X","X"," ","X"],
  ["X"," "," "," "," "," "," "," "," "," "," "," ","g","X"],
  ["X","X","X","X","X","X","X","X","X","X","X","X","X","X"]
]




start, goal = find_start_goal(maze) #busca "s" y "g" en el laberinto usando la funcion previamente descrita y los guarda en variables con dichos nombres
shortest_path = {
  "start": start,
} #se inicializa un dicionario donde se guardara el como se mueve el agente dentro del laberinto, de esta forma se logra guardar el parent de cada node
print("El laberinto a buscar una salida:\n") #imprime por pantalla un mensaje de inicio
print_maze(maze) #dibuja el laberinto en terminal
print("") #solo un salto de linea xd

if start != None and goal != None: #verifica que luego de ejecutar el "find_start_goal" se hayan obtenido dichos valores y no queden vacios

  print("Punto de inicio:", start, "\nPunto de meta: \t", goal, "\n") #imprime por pantalla el "s" y "g" identificado usando find_start_goal 
  alg = choose_algorithm() #ejecuta funcion para elegir si usar dfs o bfs o mantahann

  #ALGORITMO DE BUSQUEDA 
  frontier = [] #se inicializa la frontera 
  frontier.append(start) #se agrega a la frontera el punto de partida ya que es como si el algoritmo comenzara desde un agente que solo tiene esta frontera
  explored_set = [] #se inicializa una lista que almacena las coordenadas por las cuales el agente ya pasó
  agent = None #se inicializa el agente, el cual como comienza fuera del laberinto y solo tiene de frontera al punto de inicio queda como None
#  cont = 0 #contador arbitrario para el whi  le y saber cuantas iteraciones se han echo
  while agent != goal: #el while tiene como condición que el agente no este en la meta, si esta en la meta sale del while
#    print("\nIteración ", cont)
#    cont +=1 
    if agent != None: #verifica que el agente no sea None, es decir, que aun el algoritmo no empiece como tal, si este es diferente de none lo agregará al explored set.
      explored_set.append(agent)
#    print("explored_set: ", explored_set)
    #Si la frontera es vacía, entonces no hay solución
    if len(frontier) == 0: #verifica si el tamaño de la frontera en algun momento es 0, si es 0 el laberinto no tiene solución.
      print("\nNo hay solución para este laberinto.")
      break
    if alg == 0 or alg == -1:
      agent = frontier.pop(alg) #aca borra un nodo de la frontera en base a la decisión tomada, si se usa bfs toma 0 por lo que es una cola, si usa dfs toma -1 por lo que usa pila.
    elif alg == 3:
      k = manhatann(frontier)
      agent = frontier.pop(k)
      
#    print("Agente:", agent)
     
    frontier += find_frontiers(agent) #agrega las fronteras encontradas para el agente usando "find_frontiers" a la lista de fronteras totales, actuando como pila o cola dependiendo.
#    print("frontier: ", frontier)

  if agent == goal:
    print("\n¡Meta alcanzada!")
    sp = find_shortest_path(shortest_path)
    print("Camino mas corto con el algoritmo elegído: ", sp) 
    new_maze = draw_shortest_path(maze, sp)
    print("\nLaberinto con la solución:")
    print_maze(new_maze) 
    print("\nNodos explorados para llegar a la solución: ", explored_set)
    
elif start == None or goal == None: #verifica que luego de ejecutar el "find_start_goal" se hayan obtenido none, si es así imprime un error por pantalla y termina el programa
  print("El laberinto debe contener 's' (inicio) y 'g' (meta).")

else: #si ninguna de las 2 condiciones anteriores se cumple (raro), imprime otro mensaje de error y se termina el programa
  print("Algo ocurrio...")