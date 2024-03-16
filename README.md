# Implementation Analysis of the Graph Class
Coding Conventions Used
The implementation of the Graph class follows the coding conventions of the language in which the program is written. Descriptive method and variable names are used, following the snake_case style for most names. The class structure follows the object-oriented programming paradigm and data structures.
Proposed Solution and Implemented Algorithms
The Graph class implements a directed graph used for the construction and manipulation of finite automata. The implemented algorithms include:

Adding vertices and edges: Methods for adding vertices and edges to the graph are implemented. These methods have an average time complexity of O(1) since they only require insertion operations in a dictionary.

Displaying the graph: The display_graph() method shows the graph, involving iterating over all vertices and their neighbors. The complexity of this method is O(V + E), where V is the number of vertices and E is the number of edges in the graph.

Epsilon closure and movement: The e_closure() and move() methods use a depth-first search (DFS) algorithm to calculate epsilon closure and reachable state sets. The complexity of these methods depends on the size of the state set and the number of edges in the graph, so it can be O(V + E) in the worst-case scenario.

Subset construction: The subset_construction() method implements the subset construction algorithm to convert an NFA into a DFA. This algorithm has an exponential complexity in the worst-case scenario since it can generate an exponential number of state sets.
Asymptotic Complexity
Most implemented algorithms have a reasonable time complexity, but subset construction can be inefficient for complex NFAs with a large number of states and transitions. In these cases, the complexity can be exponential, resulting in poor performance.

## Report on the Implementation of Regular Expression to Deterministic Finite Automaton (DFA) Conversion
Language Coding Conventions:
The code follows Python PEP 8 coding conventions for code readability.
Descriptive variable names are used to improve code understanding.
Clean coding practices are followed to maintain organized and easy-to-understand code.
Reflection on the Proposed Solution:
The proposed solution utilizes a combination of algorithms, such as the infix to postfix regular expression conversion algorithm (Shunting Yard) and the subset construction algorithm to convert an NFA into a DFA.
The use of postfix notation simplifies the construction of the NFA by eliminating the need to handle operator precedence.
Asymptotic Complexity of Algorithms:
The complexity of converting the regular expression from infix to postfix is O(n), where n is the length of the regular expression.
The complexity of constructing the NFA based on the postfix regular expression is O(n), where n is the length of the regular expression.
The complexity of constructing the DFA using the subset construction algorithm depends on the number of states in the NFA and the size of the alphabet. In the worst-case scenario, it can be exponential in the number of states of the NFA.

References:

Wikipedia contributors. (2024, March 14). Shunting yard algorithm. Wikipedia. https://en.wikipedia.org/wiki/Shunting_yard_algorithm#:~:text=In%20computer%20science%2C%20the%20shunting,abstract%20syntax%20tree%20(AST).
