items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, max_cost):
    """
    Greedy algorithm for the knapsack problem.
    """
    result = []
    total_cost = 0
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )

    for item, info in sorted_items:
        if total_cost + info["cost"] <= max_cost:
            result.append(item)
            total_cost += info["cost"]

    return result


def dynamic_programming(items, max_cost):
    """
    Dynamic programming algorithm for the knapsack problem.
    """
    names = list(items.keys())
    n = len(names)
    costs = [items[name]["cost"] for name in names]
    calories = [items[name]["calories"] for name in names]

    dp = [[0] * (max_cost + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(max_cost + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    w = max_cost
    result = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            result.append(names[i - 1])
            w -= costs[i - 1]

    return list(reversed(result))


print(greedy_algorithm(items, 40))
print(dynamic_programming(items, 40))
