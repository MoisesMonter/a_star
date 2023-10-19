from typing import List, Union
import time

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.parent = None
        self.neighbors = []

def heuristic(node, goal_node):
    dx = node.x - goal_node.x
    dy = node.y - goal_node.y
    return (abs(dx) + abs(dy))*10

def a_star(maze, start, goal):
    open_set = []
    closed_set = set()

    start_node = Node(start[0], start[1])
    goal_node = Node(goal[0], goal[1])
    if (maze[start[0]][start[1]] == 1) or (maze[goal[0]][goal[1]] == 1):
        return None, None
    g_h_f_matrix = [[[] for _ in range(len(maze[0]))] for _ in range(len(maze))]

    open_set.append(start_node)

    while open_set:#enquanto tiver item aberto

        current_node = min(open_set, key=lambda node: node.f)

        open_set.remove(current_node)
        closed_set.add(current_node)

        if current_node.x == goal_node.x and current_node.y == goal_node.y:
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1], g_h_f_matrix


        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue

                new_x, new_y = current_node.x + dx, current_node.y + dy
                neighbor = Node(new_x, new_y)
                # if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] == 0:
                if neighbor not in open_set and neighbor not in closed_set and not maze[new_x][new_y] == 1:
                    neighbor.parent = current_node
                    neighbor.g = current_node.g + (10 if dx == 0 or dy == 0 else 14)
                    neighbor.h = heuristic(neighbor, goal_node)
                    neighbor.f = neighbor.g + neighbor.h
                    g_h_f_matrix[new_x][new_y] = [neighbor.g, neighbor.h, neighbor.f]
                    open_set.append(neighbor)

                elif neighbor in open_set and not maze[current_node.x][current_node.y] == 1:
                    aux_g = (10 if dx == 0 or dy == 0 else 14)

                    if neighbor.g > current_node.g + aux_g:
                        neighbor.g = current_node.g + aux_g
                        neighbor.f = neighbor.g + neighbor.h
                        g_h_f_matrix[new_x][new_y] = [neighbor.g, neighbor.h, neighbor.f]
                        neighbor.parent = current_node

    return None, g_h_f_matrix
inicio = time.time()
# Exemplo de uso
start = (0, 0)
goal = (9, 9)

# Maze representa o mapa que você forneceu
maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
        [0, 0, 1, 1, 0, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


path, g_h_f_matrix = a_star(maze, start, goal)
fim = time.time()

print(path)

import numpy as np


for row in g_h_f_matrix:
    formatted_row = []
    for value in row:
        if not value:
            formatted_row.append("[F:--- G:--- H:---]")
        else:
            formatted_value = f"[F:{int(value[2] ):<3} G:{int(value[1]):<3} H:{int(value[0] ):<3}]"
            formatted_row.append(formatted_value)
    row_string = ' '.join(formatted_row)
    print(row_string)
print(f'Tempo:{fim-inicio}')
