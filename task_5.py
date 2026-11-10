import heapq
from collections import deque

from task_4 import draw_tree, heap_to_tree


def make_colors(count):
    """Кольори у форматі #RRGGBB від темних до світлих."""
    start = (30, 90, 170)
    end = (200, 235, 255)
    colors = []
    for i in range(count):
        t = i / (count - 1) if count > 1 else 0
        r = int(start[0] + (end[0] - start[0]) * t)
        g = int(start[1] + (end[1] - start[1]) * t)
        b = int(start[2] + (end[2] - start[2]) * t)
        colors.append(f"#{r:02X}{g:02X}{b:02X}")
    return colors


def dfs(root):
    """Обхід у глибину зі стеком. Повертає вузли у порядку відвідування."""
    order = []
    stack = [root]
    while stack:
        node = stack.pop()
        order.append(node)
        # правий кладемо першим, щоб лівий вийшов зі стека раніше
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order


def bfs(root):
    """Обхід у ширину з чергою. Повертає вузли у порядку відвідування."""
    order = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order


def paint(order):
    colors = make_colors(len(order))
    for node, color in zip(order, colors):
        node.color = color


def main():
    heap = [10, 4, 7, 1, 8, 3, 6, 2, 9, 5]
    heapq.heapify(heap)

    root = heap_to_tree(heap)
    order = dfs(root)
    print("DFS:", [node.val for node in order])
    paint(order)
    draw_tree(root, "Обхід у глибину (DFS): від темних до світлих")

    root = heap_to_tree(heap)
    order = bfs(root)
    print("BFS:", [node.val for node in order])
    paint(order)
    draw_tree(root, "Обхід у ширину (BFS): від темних до світлих")


if __name__ == "__main__":
    main()
