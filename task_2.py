import matplotlib.pyplot as plt


def draw_square(ax, p0, p1, level):
    """Малює квадрат на відрізку p0-p1 і два менші квадрати над ним."""
    ux = p1[0] - p0[0]
    uy = p1[1] - p0[1]
    # вектор "вгору" відносно основи: основа повернута на 90 градусів
    vx = -uy
    vy = ux

    a = (p0[0] + vx, p0[1] + vy)
    b = (p1[0] + vx, p1[1] + vy)
    ax.fill([p0[0], p1[0], b[0], a[0]], [p0[1], p1[1], b[1], a[1]],
            color="saddlebrown" if level > 2 else "forestgreen", edgecolor="black", linewidth=0.3)

    if level == 0:
        return

    # вершина прямокутного трикутника над верхньою стороною квадрата
    c = (a[0] + 0.5 * ux + 0.5 * vx, a[1] + 0.5 * uy + 0.5 * vy)
    draw_square(ax, a, c, level - 1)
    draw_square(ax, c, b, level - 1)


def main():
    level = int(input("Введіть рівень рекурсії (наприклад, 8): "))

    fig, ax = plt.subplots(figsize=(8, 6))
    draw_square(ax, (-0.5, 0), (0.5, 0), level)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(f"Дерево Піфагора, рівень {level}")
    plt.show()


if __name__ == "__main__":
    main()
