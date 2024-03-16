import DataStructures as ds  # Importar la clase Graph definida en otro archivo


def convert_regex_to_postfix(expression, characters, operators):
  """
    Convertir una expresión regular a notación postfix.
    Complejidad: O(n), donde n es la longitud de la expresión regular.
    """
  output_queue = []
  operator_stack = []

  for token in expression:
    if token in characters:  # Verificar si el token es un caracter
      output_queue.append(token)
    elif token in operators:  # Verificar si el token es un operador
      if operators[token][1] == "right":
        output_queue.append(token)
      else:
        while operator_stack and operator_stack[-1] != "(" and (
            operators[operator_stack[-1]][0] > operators[token][0] or
            (operators[operator_stack[-1]][0] == operators[token][0]
             and operators[token][1] == "left")):
          output_queue.append(operator_stack.pop())
        operator_stack.append(token)
    elif token == "(":  # Manejar paréntesis izquierdo
      operator_stack.append(token)
    elif token == ")":  # Manejar paréntesis derecho
      while operator_stack[-1] != "(":
        if not operator_stack:
          return 0
        output_queue.append(operator_stack.pop())
      operator_stack.pop()

  while operator_stack:  # Vaciar la pila de operadores
    if operator_stack[-1][0] == "(":
      return 0
    output_queue.append(operator_stack.pop())

  return ''.join(output_queue)  # Unir la cola de salida en una cadena


def concatenate_regex(regex, alphabet):
  """
    Concatenar símbolos con '/' donde sea necesario en la expresión regular.
    Complejidad: O(n), donde n es la longitud de la expresión regular.
    """
  concatenated = ""
  i = 0
  while i < len(regex):
    if regex[i] in alphabet and i + 1 < len(regex) and (
        regex[i + 1] in alphabet or regex[i + 1] == "(") or (regex[i] == "*"
                                                           or regex[i] == "+"):
      concatenated += regex[i] + '/'
    else:
      concatenated += regex[i]
    i += 1
  return concatenated


def construct_graph(postfix, index, exp, graph, vertex_count):
  """
    Construir un grafo NFA basado en la expresión regular en notación postfix.
    Complejidad: O(n), donde n es la longitud de la expresión regular postfix.
    """
  if index < len(postfix):
    if postfix[index] == "|":
      if len(exp) > 1:
        new_exp = []
        graph.add_edge(vertex_count, exp[-2][0], "#")
        graph.add_edge(vertex_count, exp[-1][0], "#")
        new_exp.append(vertex_count)
        vertex_count += 1

        graph.add_edge(exp[-1][1], vertex_count, "#")
        graph.add_edge(exp[-2][1], vertex_count, "#")
        new_exp.append(vertex_count)
        vertex_count += 1

        exp.pop()
        exp.pop()
        exp.append(new_exp)
    elif postfix[index] == "*":
      if len(exp) > 0:
        new_exp = []
        graph.add_edge(exp[-1][1], exp[-1][0], "#")
        graph.add_edge(vertex_count, exp[-1][0], "#")
        graph.add_edge(vertex_count, vertex_count + 1, "#")
        new_exp.append(vertex_count)
        vertex_count += 1

        graph.add_edge(exp[-1][1], vertex_count, "#")
        new_exp.append(vertex_count)
        vertex_count += 1

        exp.pop()
        exp.append(new_exp)
    elif postfix[index] == "+":
      if len(exp) > 0:
        new_exp = []
        graph.add_edge(exp[-1][1], exp[-1][0], "#")
        graph.add_edge(vertex_count, exp[-1][0], "#")

        new_exp.append(vertex_count)
        vertex_count += 1

        graph.add_edge(exp[-1][1], vertex_count, "#")
        new_exp.append(vertex_count)
        vertex_count += 1

        exp.pop()
        exp.append(new_exp)
    elif postfix[index] == "/":
      if len(exp) > 1:
        graph.add_edge(exp[-2][1], exp[-1][0], "#")
        new_exp = [exp[-2][0], exp[-1][1]]

        exp.pop()
        exp.pop()
        exp.append(new_exp)
    elif postfix[index] in characters:
      graph.add_edge(vertex_count, vertex_count + 1, postfix[index])
      exp.append([vertex_count, vertex_count + 1])
      vertex_count += 2
    return construct_graph(postfix, index + 1, exp, graph, vertex_count)
  else:
    return exp, graph


characters = []
operators = {
    "|": (3, "left"),
    "*": (3, "right"),
    "+": (2, "right"),
    "/": (4, "left"),
}

alphabet = input("Alphabet: ")

for i in alphabet:
  characters.append(i)

regex = input("RegEX: ")

concatenated = concatenate_regex(regex, alphabet)
postfix = convert_regex_to_postfix(concatenated, characters, operators)
postfix = str(postfix)

graph = ds.Graph()  # Crear un objeto de la clase Graph
exp, graph = construct_graph(postfix, 0, [], graph,
                             0)  # Construir el grafo NFA

print("\n----RESULTS----")
print("INPUT:")
print(regex, "\n")

print("NFA: ")
graph.display_graph()  # Mostrar el grafo NFA
print("Accepting state: ", exp[0][1], "\n")

start_state = [exp[0][0]]
final_state = exp[0][1]

index = 0

graph.subset_construction(
    start_state, characters,
    final_state)  # Realizar la construcción de subconjuntos del DFA
