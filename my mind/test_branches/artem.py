from collections import deque

def find_path_with_least_turns(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Список направлений: вниз, вправо, вверх, влево
    queue = deque([(start, 0, None)])  # Очередь с элементами: (координаты, количество поворотов, предыдущая ячейка)
    visited = set([start])  # Множество уже посещенных ячеек
    
    while queue:
        current, turns, prev = queue.popleft()
        if current == end:
            return reconstruct_path(prev, current)
        
        for dx, dy in directions:
            x, y = current[0] + dx, current[1] + dy
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0:
                new_turns = turns
                if prev and get_direction(prev, current) != get_direction(current, (x, y)):
                    new_turns += 1
                neighbor = (x, y)
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, new_turns, current))
    
    return None  # Если путь не найден

def get_direction(source, destination):
    dx = destination[0] - source[0]
    dy = destination[1] - source[1]
    if dx == 1:
        return "down"
    elif dx == -1:
        return "up"
    elif dy == 1:
        return "right"
    elif dy == -1:
        return "left"
    else:
        return None

def reconstruct_path(prev_dict, current):
    path = []
    while current:
        path.append(current)
        print(prev_dict)
    return list(reversed(path))


grid = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 4)
end = (4, 0)

path = find_path_with_least_turns(grid, start, end)
print(path) 