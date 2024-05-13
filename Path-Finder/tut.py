import curses
from curses import wrapper
from queue import Queue
import time

ques_maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]


def find_start(maze, start="O"):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j


def find_neighbours(maze, curr):
    length = len(maze[0])
    x, y = curr
    # print("yes")
    neighbours = []
    if x > 0:  # Up
        # print("x > 0")
        neighbours.append((x-1, y))
    if y < length:  # Right
        # print("y < length")
        neighbours.append((x, y+1))
    if x < length:  # Down
        # print("x < length")
        neighbours.append((x+1, y))
    if y > 0:  # Left
        # print("y > 0")
        neighbours.append((x, y-1))
    # print(f"The current neighbours are: {neighbours}")

    return neighbours


def print_maze(maze, stdscr, visited):
    magenta = curses.color_pair(1)
    cyan = curses.color_pair(2)
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in visited:
                stdscr.addstr(i, j*2, "x", magenta)
            if value == "#":
                stdscr.addstr(i, j*2, value, cyan)


def find_path(maze, stdscr=None):
    start = "O"
    end = "X"
    curr = find_start(maze, start)
    visited = set()
    q = Queue()
    q.put((curr, [curr]))
    while not q.empty():
        curr_pos, path = q.get()
        # print(f"The curr pos is: {curr_pos}")
        x, y = curr_pos
        # print(x, y)

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.1)
        stdscr.refresh()

        neighbours = find_neighbours(maze, curr_pos)

        if maze[x][y] == end:
            return path

        for neighbour in neighbours:
            r, c = neighbour
            # print(maze[r][c])
            # print(visited)
            if neighbour in visited:
                continue
            if maze[r][c] == "#":
                continue
            new_path = path + [neighbour]
            # print(new_path)
            q.put((neighbour, new_path))
            visited.add(neighbour)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    find_path(ques_maze, stdscr)
    stdscr.addstr(10, 0, "This is the shortest path.")
    stdscr.getch()


wrapper(main)
