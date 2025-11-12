
def read_maze_from_file(filename):
    """Reads a maze text file and converts it into a numeric grid."""
    maze = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line:  # ignore empty lines
                row = [1 if c == '.' else 0 for c in line]
                maze.append(row)
    return maze


def print_solution_with_path(maze, solution):
    """Prints maze showing path as 'P', wall as '#', open path as '.'"""
    n = len(maze)
    for i in range(n):
        line = ""
        for j in range(n):
            if maze[i][j] == 0:
                line += "#"
            elif solution[i][j] == 1:
                line += "P"
            else:
                line += "."
        print(line)
    print()


def is_safe(maze, x, y, solution, n):
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 1 and solution[x][y] == 0


def solve_maze_util(maze, x, y, solution, n):
    # Base case: reached destination
    if x == n - 1 and y == n - 1 and maze[x][y] == 1:
        solution[x][y] = 1
        print("✅ Path found:")
        print_solution_with_path(maze, solution)
        return True

    if is_safe(maze, x, y, solution, n):
        # Mark current cell as part of the solution path
        solution[x][y] = 1

        # Move Down
        if solve_maze_util(maze, x + 1, y, solution, n):
            return True

        # Move Right
        if solve_maze_util(maze, x, y + 1, solution, n):
            return True

        # Move Up
        if solve_maze_util(maze, x - 1, y, solution, n):
            return True

        # Move Left
        if solve_maze_util(maze, x, y - 1, solution, n):
            return True

        # Backtrack
        solution[x][y] = 0
        return False

    return False


def solve_maze_from_file(filename):
    maze = read_maze_from_file(filename)
    n = len(maze)
    if n == 0:
        print("Maze file is empty!")
        return

    solution = [[0] * n for _ in range(n)]

    if not solve_maze_util(maze, 0, 0, solution, n):
        print("No path found 😿")


def print_maze(m):
    for row in m:
        print(row)

# Example usage
if __name__ == "__main__":
    solve_maze_from_file("maze.txt")