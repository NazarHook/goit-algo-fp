items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    """Жадібний вибір: спершу страви з найбільшим співвідношенням калорій до вартості."""
    names = sorted(items, key=lambda name: items[name]["calories"] / items[name]["cost"], reverse=True)
    chosen = []
    total_cost = 0
    total_calories = 0
    for name in names:
        cost = items[name]["cost"]
        if total_cost + cost <= budget:
            chosen.append(name)
            total_cost += cost
            total_calories += items[name]["calories"]
    return chosen, total_cost, total_calories


def dynamic_programming(items, budget):
    """Задача про рюкзак: table[i][b] це максимум калорій з перших i страв при бюджеті b."""
    names = list(items)
    n = len(names)
    table = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost = items[names[i - 1]]["cost"]
        calories = items[names[i - 1]]["calories"]
        for b in range(budget + 1):
            table[i][b] = table[i - 1][b]
            if cost <= b:
                with_item = table[i - 1][b - cost] + calories
                if with_item > table[i][b]:
                    table[i][b] = with_item

    # відновлюємо набір страв, рухаючись по таблиці назад
    chosen = []
    b = budget
    for i in range(n, 0, -1):
        if table[i][b] != table[i - 1][b]:
            name = names[i - 1]
            chosen.append(name)
            b -= items[name]["cost"]
    chosen.reverse()

    total_cost = sum(items[name]["cost"] for name in chosen)
    return chosen, total_cost, table[n][budget]


def main():
    budget = 100
    print(f"Бюджет: {budget}")

    chosen, cost, calories = greedy_algorithm(items, budget)
    print("Жадібний алгоритм:", chosen, "вартість", cost, "калорії", calories)

    chosen, cost, calories = dynamic_programming(items, budget)
    print("Динамічне програмування:", chosen, "вартість", cost, "калорії", calories)


if __name__ == "__main__":
    main()
