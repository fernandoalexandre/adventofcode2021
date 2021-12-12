
def read_file(path: str) -> list:
    with open(path) as fp:
        return fp.readlines()

def have_a_walk(graph: dict, cave: str, visited):
    visited.append(cave)
    
    full_visited_list = []
    for path in graph[cave]:
        if path == "end":
            finished_visited = visited.copy()
            finished_visited.append("end")

            full_visited_list.append(finished_visited)
        elif (path.islower() and path in visited) or path == "start":
            continue
        else:
            rec_visited = visited.copy()
            visited_list = have_a_walk(graph, path, rec_visited)
            for path in visited_list:
                if len(visited_list) != 0 and path[-1] == "end":
                    full_visited_list.append(path)

    return full_visited_list

def have_a_walk_p2(graph: dict, cave: str, visited, already_visited_twice):
    visited.append(cave)
    
    full_visited_list = []
    for path in graph[cave]:
        if path == "end":
            finished_visited = visited.copy()
            finished_visited.append("end")

            full_visited_list.append(finished_visited)
        elif path == "start":
            continue
        elif (path.islower() and path in visited):
            if already_visited_twice:
                continue
            else:
                rec_visited = visited.copy()
                visited_list = have_a_walk_p2(graph, path, rec_visited, True)
                for path in visited_list:
                    if len(visited_list) != 0 and path[-1] == "end":
                        full_visited_list.append(path)
        else:
            rec_visited = visited.copy()
            visited_list = have_a_walk_p2(graph, path, rec_visited, already_visited_twice)
            for path in visited_list:
                if len(visited_list) != 0 and path[-1] == "end":
                    full_visited_list.append(path)

    return full_visited_list

def main():
    content = read_file("day12/input")

    part1 = 0
    part2 = 1
    graph = {}

    
    for line in content:
        source, dst = line.rstrip("\n").split("-")
        if source not in graph:
            graph[source] = []
    
        if dst not in graph:
            graph[dst] = []

        if dst not in graph[source]:
            graph[source].append(dst)
        
        if source not in graph[dst] and source != "start":
            graph[dst].append(source)
            
    
    full_list = []
    print("==== Part 1 ====")
    for path in graph["start"]:
        full_list.extend(have_a_walk(graph, path, ["start"]))

    for path in full_list:
        print(path)

    part1 = len(full_list)

    full_list = []

    print("==== Part 2 ====")
    for path in graph["start"]:
        full_list.extend(have_a_walk_p2(graph, path, ["start"], False))

    for path in full_list:
        print(path)
    
    part2 = len(full_list)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")



if __name__ == "__main__":
    main()