import curses
from curses import wrapper
from queue import Queue

q1 = Queue()
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


def print_maze(maze, stdscr, path=None):
    magenta = curses.color_pair(1)
    for i, rows in enumerate(maze):
        for j, col in enumerate(rows):
            stdscr.addstr(i, j*3, col, magenta)
    if path is None:
        path = []


def neighbour(current_pos, length, visited, l1):
    # print("yes")
    x, y = current_pos
    if x > 0:
        if (x-1, y) not in visited and (x-1, y) not in l1:
            # print("x > 0")
            q1.put((x-1, y))
    if y < length:
        if (x, y+1) not in visited and (x, y+1) not in l1:
            # print("y < length")
            q1.put((x, y+1))
    if x < length:
        if (x+1, y) not in visited and (x+1, y) not in l1:
            # print("x < length")
            q1.put((x+1, y))
    if y > 0:
        if (x, y-1) not in visited and (x, y-1) not in l1:
            # print("y > 0")
            q1.put((x, y-1))
    """
    x > 0 up
    y < len right
    x < len down
    y > 0 left
    """


def find_path(maze):
    start = None
    end = None
    visited = set()
    length = len(maze[0])
    found = False
    # print(f"this is the length {length}")
    for i, rows in enumerate(maze):
        for j, col in enumerate(rows):
            if maze[i][j] == "O":
                start = (i, j)
            if maze[i][j] == "X":
                end = (i, j)
    q1.put(start)

    while not q1.empty():
        l1 = list(q1.queue)
        # print(l1)
        curr = q1.get()
        # print(visited)
        print(f"current element is: {curr}")
        if curr not in visited:
            visited.add(curr)
        neighbour(curr, length, visited, l1)
        # print(f"hell {q1.qsize()}")


def main(stdscr):
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    stdscr.clear()
    print_maze(ques_maze, stdscr)
    stdscr.refresh()
    stdscr.getkey()


# wrapper(main)
find_path(ques_maze)
