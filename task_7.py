import random

import matplotlib.pyplot as plt

ROLLS = 1_000_000


def simulate(rolls):
    """Кидає два кубики rolls разів, повертає ймовірність кожної суми від 2 до 12."""
    counts = {total: 0 for total in range(2, 13)}
    for _ in range(rolls):
        total = random.randint(1, 6) + random.randint(1, 6)
        counts[total] += 1
    return {total: count / rolls for total, count in counts.items()}


def analytic():
    """Точні ймовірності: кількість комбінацій з 36 можливих."""
    result = {}
    for total in range(2, 13):
        ways = 6 - abs(total - 7)
        result[total] = ways / 36
    return result


def main():
    random.seed(42)
    monte_carlo = simulate(ROLLS)
    exact = analytic()

    print(f"Кидків: {ROLLS}")
    print("Сума | Монте-Карло | Аналітично | Різниця")
    for total in range(2, 13):
        mc = monte_carlo[total] * 100
        an = exact[total] * 100
        print(f"{total:>4} | {mc:>10.2f}% | {an:>9.2f}% | {mc - an:+.2f}%")

    sums = list(range(2, 13))
    plt.bar([s - 0.2 for s in sums], [monte_carlo[s] * 100 for s in sums], width=0.4, label="Монте-Карло")
    plt.bar([s + 0.2 for s in sums], [exact[s] * 100 for s in sums], width=0.4, label="Аналітично")
    plt.xlabel("Сума")
    plt.ylabel("Ймовірність, %")
    plt.xticks(sums)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
