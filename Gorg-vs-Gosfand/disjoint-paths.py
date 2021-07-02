from turtle import *

from time import *


def number_to_point(n):
    x = (n % 5 * 50 + 25) - 125
    y = (n // 5 * 50) - 125
    return x, y


def point_to_number(x, y):
    row = (y + 125) // 50
    col = (x + 125) // 50
    n = int(row * 5 + col)


def show_number(n):
    lt(90)
    fd(12.5)
    write(n)
    bk(12.5)
    rt(90)


def draw_circle(n):
    if n != 0:
        pensize(6)
        color("purple")
        pendown()
    else:
        pu()
    goto(number_to_point(n))
    pensize(4)
    color("cyan")

    pu()
    show_number(n)
    pendown()
    circle(18)
    penup()


def graphic_routing(result):
    for i in result:
        draw_circle(i)


def bfs(graph, s, t, foot_step):
    v_length = len(graph)
    visited = [False] * (v_length)
    queue = []
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.pop(0)
        for index, value in enumerate(graph[u]):
            if not (visited[index]) and value > 0:
                queue.append(index)
                visited[index] = True
                foot_step[index] = u
    return visited[t]


def show_path(foot_step):
    path = [len(foot_step) - 1]
    v = foot_step[-1]
    while v != 0:
        path.append(v)
        v = foot_step[v]
    path.append(0)
    return path[::-1]


def disjoint_path(graph, source, sink):
    v_length = len(graph)
    foot_step = [-1] * (v_length)
    max_flow = 0
    while bfs(graph, source, sink, foot_step):
        path = show_path(foot_step)
        print("Path: ", *path)
        graphic_routing(path)
        sleep(1)
        clear()
        path_flow = float("Inf")
        s = sink
        while (s != source):
            path_flow = min(path_flow, graph[foot_step[s]][s])
            s = foot_step[s]

        max_flow += path_flow

        v = sink
        while (v != source):
            u = foot_step[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = foot_step[v]


def main():
    graph = [[0, 1, 1, 1, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 1, 0, 0, 0, 0, 1],
             [0, 1, 0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 1, 0, 1],
             [0, 0, 0, 0, 0, 0, 0, 0]]

    source = 0;
    sink = 7
    disjoint_path(graph, source, sink)


if __name__ == "__main__":
    main()
