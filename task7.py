import random
from rich.console import Console
from rich.table import Table

analytical_probabilities = {
    2: (1 / 36) * 100,
    3: (2 / 36) * 100,
    4: (3 / 36) * 100,
    5: (4 / 36) * 100,
    6: (5 / 36) * 100,
    7: (6 / 36) * 100,
    8: (5 / 36) * 100,
    9: (4 / 36) * 100,
    10: (3 / 36) * 100,
    11: (2 / 36) * 100,
    12: (1 / 36) * 100,
}


def throw_two_dices():
    """
    Throw 2 dices
    """
    return random.randint(1, 6) + random.randint(1, 6)


def get_probabilities(n=1000000):
    """
    Get probabilities of throwing n dices
    """
    probabilities = {
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0,
    }
    i = n
    while i > 0:
        result = throw_two_dices()
        probabilities[result] += 1
        i -= 1
    for key, value in probabilities.items():
        probabilities[key] = (value / n) * 100
    return probabilities


def print_table(probabilities, analytical_probabilities):
    """
    Print table of probabilities
    """
    table = Table(title="Probabilities of throwing 2 dices")

    table.add_column("Sum", style="cyan")
    table.add_column("Probability (%)", style="green")
    table.add_column("Analytical Probability (%)", style="red")
    table.add_column("Difference (%)", style="blue")

    for sum_value, probability in probabilities.items():
        table.add_row(
            str(sum_value),
            f"{probability:.2f}",
            f"{analytical_probabilities[sum_value]:.2f}",
            f"{probability - analytical_probabilities[sum_value]:.2f}",
        )

    console = Console()
    console.print(table)


print_table(get_probabilities(), analytical_probabilities)
