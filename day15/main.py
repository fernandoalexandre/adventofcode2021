from queue import PriorityQueue

class Graph():
    def __init__(self):
        self.edges = {}
        self.visited = {}
    
    def add_link(self, src: str, dst: str, weight: int):
        if src in self.edges:
            self.edges[src][dst] = weight
        else:
            self.edges[src] = {dst: weight}
        
    def find_shortest_part1(self, src):
        D = {}
        D[src] = 0

        pq = PriorityQueue()
        pq.put((0, src))

        while not pq.empty():
            (_, curr_vertex) = pq.get()
            self.visited[curr_vertex] = 1

            for neighbor in self.edges[curr_vertex].keys():
                distance = self.edges[curr_vertex][neighbor]
                if neighbor not in self.visited:
                    if neighbor in D:
                        old_cost = D[neighbor]
                    else:
                        old_cost = float('inf')
                    new_cost = D[curr_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost

        return D
       

def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()

def is_valid(i, j, n, m):
    return 0 <= i <= n and 0 <= j <= m

def amplify(map):
    # Your original map tile repeats to the right and downward;
    # each time the tile repeats to the right or downward, all of its risk levels are 1 higher than the tile immediately up or left of it.
    # risk levels above 9 wrap back around to 1
    new_map = [[0 for _ in range(0, len(map[0])*5)] for _ in range(0, len(map)*5)]

    for i in range(0, 5):
        for j in range(0, 5):
            for k in range(0, len(map)):
                for l in range(0, len(map[0])):
                    val = map[k][l] + i + j
                    if val > 9:
                        val = val % 9
                    new_map[i*len(map)+k][j*len(map[0]) + l] = val
    
    #for line in new_map:
    #    print(*line)
    
    return new_map

def part1(map):
    part1 = 0

    graph = Graph()
    for i in range(0, len(map)):
        for j in range(0, len(map[0])):
            current = f"{i:02d}{j:02d}"

            slots = [
                [i+1, j],
                [i, j+1],
                [i-1, j],
                [i, j-1]
            ]

            for row, col in slots:
                if is_valid(row, col, len(map)-1, len(map[0])-1):
                    dst = f"{row:02d}{col:02d}"
                    graph.add_link(current, dst, map[row][col])

    destination = f"{len(map)-1:02d}{len(map[0])-1:02d}"
    part1 = graph.find_shortest_part1("0000")

    print(f"Part 1: {part1[destination]}")

    return part1

def part2(map):
    # configure new map:
    new_map = amplify(map)

    part2 = 0

    graph = Graph()
    for i in range(0, len(new_map)):
        for j in range(0, len(new_map[0])):
            current = f"{i:04d}{j:04d}"

            slots = [
                [i+1, j],
                [i, j+1],
                [i-1, j],
                [i, j-1]
            ]

            for row, col in slots:
                if is_valid(row, col, len(new_map)-1, len(new_map[0])-1):
                    dst = f"{row:04d}{col:04d}"
                    graph.add_link(current, dst, new_map[row][col])

    destination = f"{len(new_map)-1:04d}{len(new_map[0])-1:04d}"
    part2 = graph.find_shortest_part1("00000000")

    print(f"Part 2: {part2[destination]}")

    return part2

def main():
    content = read_file("day15/input")

    risk_map = []

    for line in content:
        risk_map.append(list(map(int, list(line.rstrip("\n")))))

    print("-------------- Part 1 ------------------")

    p1 = part1(risk_map)

    print("-------------- Part 2 ------------------")

    p2 = part2(risk_map)

if __name__ == "__main__":
    main()