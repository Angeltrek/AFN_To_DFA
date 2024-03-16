class Graph:
  """
  Clase que representa un grafo.
  """

  def __init__(self):
    """
      Inicializa el grafo como un diccionario vacío.
      Complejidad: O(1)
      """
    self.graph = {}

  def add_vertex(self, vertex):
    """
      Añade un nuevo vértice al grafo con una lista vacía de vecinos.
      Complejidad: O(1)
      """
    if vertex not in self.graph:
      self.graph[vertex] = []

  def add_edge(self, source, destination, label):
    """
      Añade una arista al grafo entre dos vértices con una etiqueta dada.
      Si los vértices no están en el grafo, los añade.
      Complejidad: O(1) promedio, O(n) peor caso (donde n es el número de vecinos del vértice fuente)
      """
    if source not in self.graph:
      self.add_vertex(source)
    if destination not in self.graph:
      self.add_vertex(destination)
    self.graph[source].append((destination, label))

  def display_graph(self):
    """
      Muestra cada vértice y su lista de vecinos en el grafo.
      Complejidad: O(V + E), donde V es el número de vértices y E es el número de aristas en el grafo.
      """
    for vertex, neighbors in self.graph.items():
      print(f"{vertex} => {neighbors}")

  def get_neighbors(self, vertex):
    """
      Devuelve una lista de vecinos para un vértice dado.
      Complejidad: O(1) promedio, O(n) peor caso (donde n es el número de vecinos del vértice)
      """
    if vertex in self.graph:
      return [(neighbor[0], neighbor[1]) for neighbor in self.graph[vertex]]
    else:
      return []

  def e_closure(self, T):
    """
      Calcula el cierre épsilon para un conjunto de estados dados.
      Complejidad: O(V + E), donde V es el número de vértices y E es el número de aristas en el grafo.
      """
    stack = []
    stack.extend(T)
    e_closure_set = set(T)
    while stack:
      t = stack.pop()
      for u, label in self.get_neighbors(t):
        if label == '#' and u not in e_closure_set:
          e_closure_set.add(u)
          stack.append(u)
    return sorted(e_closure_set)

  def move(self, T, a):
    """
      Calcula el conjunto de estados alcanzables por el símbolo de entrada 'a' desde un conjunto de estados dado.
      Complejidad: O(V), donde V es el número de vértices en el grafo.
      """
    move_set = []
    for state in T:
      neighbors = self.get_neighbors(state)
      for neighbor, label in neighbors:
        if label == a:
          move_set.append(neighbor)
    return move_set

  def subset_construction(self, start_state, alphabet, final_state):
    """
      Realiza la construcción de subconjuntos para convertir un NFA a un DFA.
      Complejidad: O(2^V * V), donde V es el número de vértices en el grafo.
      """
    Dstates = [self.e_closure(start_state)]  # Lista de conjuntos de estados
    Dtran = []  # Tabla de transiciones
    ctr = 0
    dic = {
        ctr: 0
    }  # Diccionario para hacer seguimiento de las asignaciones de estados
    s_ctr = 0
    dfa = {}
    current = Dstates[0]
    final_states = []

    self.dfa_auxiliary(Dstates, Dtran, alphabet, current, ctr, dic, dfa, s_ctr)

    print("DFA:")
    for key, value in dfa.items():
      print(f"{chr(key + 65)} => {value}")

    for Dstate in Dstates:
      if final_state in Dstate:
        final_states.append(chr(Dstates.index(Dstate) + 65))

    print("Accepting states: ", final_states)

    return Dstates, Dtran

  def dfa_auxiliary(self, Dstates, Dtran, alphabet, current, ctr, dic, dfa,
                    s_ctr):
    """
      Función auxiliar para realizar la construcción de subconjuntos del DFA.
      Complejidad: O(2^V * V), donde V es el número de vértices en el grafo.
      """
    new_move = []

    for a in alphabet:
      move = self.move(current, a)
      if move not in Dtran and move != []:
        dic[ctr] = move
        ctr += 1
      for key, value in dic.items():
        if value == move:
          new_move.append((chr((key + 1) + 65), a))
      Dtran.append(move)

    dfa[s_ctr] = new_move

    for Dtran_value in Dtran:
      new_state = self.e_closure(Dtran_value)
      if new_state not in Dstates and new_state != []:
        Dstates.append(new_state)
        self.dfa_auxiliary(Dstates, Dtran, alphabet, new_state, ctr, dic, dfa,
                           s_ctr + 1)

    return
