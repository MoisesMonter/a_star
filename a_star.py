
from decouple import config

Horizontal_vertical = config("Horizontal_vertical")
Diagonal = config("Diagonal")



class Node:
    def __init__(self, position, end, g=0, h=0, parent=None):
        self.rato = position
        self.vizinho = {"7":[False,[-1,-1]],"8":[False,[-1, 0]],"9":[False,[-1,+1]],
                        "4":[False,[-1, 0]]                    ,"6":[False,[ 0,+1]],
                        "1":[False,[+1,-1]],"2":[False,[+1, 0]],"3":[False,[ +1,+1]]}
        self.g = g  # Custo G (custo do caminho do início até este nó)
        self.h = h  # Custo H (heurística - custo estimado do nó até o objetivo)
        self.f = g + h  # Custo F (soma de G e H)
        self.parent = parent  # Referência ao nó pai (nó do qual este nó foi alcançado)
        self.queijo = end  

    def set_goal(self, goal_position):
        self.goal = goal_position

def heuristic(node):
    # Calcula a distância de Manhattan do nó atual até o objetivo
    if node.queijo is not None:
        x1, y1 = node.rato
        x2, y2 = node.queijo
        node.h= (abs(x1 - x2) + abs(y1 - y2))*Horizontal_vertical
    else:
        return -1  # Se a posição do objetivo não estiver definida, retornamos 0

# Exemplo de uso:
# Partida = (0,0)
# Fim = (9, 9)  # Substitua pelas coordenadas do seu objetivo
# node = Node(Partida,Fim)
# heuristic_value = heuristic(node)
# print("Heurística:", node.h)