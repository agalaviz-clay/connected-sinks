class ConnectedSinks:
    def find_connected_sinks(self, file_path):
        graph, source_row, source_col = self.create_graph_and_find_source(file_path)

        # DFS set up
        list_found_sink = []
        visited = set()
        directions_dict = {}  
        up = [-1, 0]
        down = [1, 0]
        left = [0, -1]
        right = [0, 1]
        directions_dict['═'] = [left, right]
        directions_dict['║'] = [up, down]
        directions_dict['╔'] = [down, right]
        directions_dict["╗"] = [down, left]
        directions_dict["╚"] = [up, right]
        directions_dict["╝"] = [up, left]
        directions_dict["╠"] = [up, down, right]
        directions_dict["╣"] = [up, down, left]
        directions_dict["╦"] = [down, left, right]
        directions_dict["╩"] = [up, left, right]

        self.dfs(source_row, source_col, graph, list_found_sink, directions_dict, visited)
        sorted_list = sorted(list_found_sink)
        return ''.join(sorted_list)

    def create_graph_and_find_source(self, file_path):
        graph = []
        source_location = None

        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                components = line.strip().split()

                obj_char, x, y = components

                x, y = int(x), int(y)

                while len(graph) <= y:
                    graph.append([' '] * (x + 1))

                for row in graph:
                    while len(row) <= x:
                        row.append(' ')

                # Place the object character in the graph
                graph[y][x] = obj_char

                if obj_char == '*':
                    source_location = (y, x)

        # Calculate the rows and columns for the source location
        rows, cols = source_location
        rows = len(graph) - 1 - rows

        graph.reverse()

        return graph, rows, cols

    def dfs(self, row, col, graph, list_found_sink, directions_dict, visited):
        rows = len(graph)
        cols = len(graph[0])
        if (row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited or graph[row][col] == ' '):
            return

        visited.add((row, col))

        # Check if at a sink
        cur_char = graph[row][col]
        if 'A' <= cur_char <=  'Z':
            list_found_sink.append(graph[row][col])

        # Call dfs
        if cur_char == '*' or 'A' <= cur_char <= 'Z':
            if self.has_path(row, col, row - 1, col, graph, directions_dict):
                self.dfs(row - 1, col, graph, list_found_sink, directions_dict, visited)
            if self.has_path(row, col, row + 1, col, graph, directions_dict):
                self.dfs(row + 1, col, graph, list_found_sink, directions_dict, visited)
            if self.has_path(row, col, row, col - 1, graph, directions_dict):
                self.dfs(row, col - 1, graph, list_found_sink, directions_dict, visited)
            if self.has_path(row, col, row, col + 1, graph, directions_dict):
                self.dfs(row, col + 1, graph, list_found_sink, directions_dict, visited)
        else: 
            if cur_char in directions_dict:
                directions_list = directions_dict[cur_char]
                for direction in directions_list:
                    next_row = row + direction[0]
                    next_col = col + direction[1]
                    if self.has_path(row, col, next_row, next_col, graph, directions_dict):
                        self.dfs(next_row, next_col, graph, list_found_sink, directions_dict, visited)   

    def has_path(self, current_row, current_col, next_row, next_col, graph, directions_dict):
        rows = len(graph)
        cols = len(graph[0])

        if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
            return False
        
        if graph[next_row][next_col] == ' ':
            return False
        
        if 'A' <= graph[next_row][next_col] <= 'Z':
            return True
        
        next_char = graph[next_row][next_col]
        if next_char in directions_dict:
                directions_list = directions_dict[next_char]
                for direction in directions_list:
                    potential_row = next_row + direction[0]
                    potential_col = next_col + direction[1]
                    if potential_row == current_row and potential_col == current_col:
                        return True
                return False

def main():
    file = "pipes_and_sinks.txt"
    connected_sinks = ConnectedSinks()
    print(connected_sinks.find_connected_sinks(file))

if __name__ == "__main__":
    main()
