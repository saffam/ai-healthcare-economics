
"""
Economic calculation validation program.

The values used here are artificial test values.
They are NOT NHS data or research findings.
"""


def total_cost(unit_cost, quantity):
    if unit_cost < 0 or quantity < 0:
        raise ValueError("Costs and quantities cannot be negative.")
    return unit_cost * quantity


def cost_per_person(total_cost_value, population):
    if total_cost_value < 0:
        raise ValueError("Cost cannot be negative.")
    if population <= 0:
        raise ValueError("Population must be positive.")
    return total_cost_value / population


def incremental_cost(intervention, comparator):
    return intervention - comparator


def incremental_effect(intervention, comparator):
    return intervention - comparator


def calculate_icer(additional_cost, additional_effect):
    if additional_effect == 0:
        return None
    return additional_cost / additional_effect


def diagnostic_classification(population, prevalence, sensitivity, specificity):
    for value in (prevalence, sensitivity, specificity):
        if not 0 <= value <= 1:
            raise ValueError("Proportions must be between zero and one.")

    if population < 0:
        raise ValueError("Population cannot be negative.")

    people_with_condition = population * prevalence
    people_without_condition = population - people_with_condition

    return {
        "true_positives": people_with_condition * sensitivity,
        "false_negatives": people_with_condition * (1 - sensitivity),
        "true_negatives": people_without_condition * specificity,
        "false_positives": people_without_condition * (1 - specificity),
    }


def run_tests():
    print("Testing economic calculations...")
    print("All test values are artificial.")
    print()

    assert total_cost(10, 100) == 1000
    print("PASS: Total cost")

    assert cost_per_person(1000, 100) == 10
    print("PASS: Cost per person")

    assert incremental_cost(1200, 1000) == 200
    print("PASS: Incremental cost")

    assert incremental_effect(80, 60) == 20
    print("PASS: Incremental effect")

    assert calculate_icer(200, 20) == 10
    print("PASS: Incremental cost-effectiveness ratio")

    assert calculate_icer(200, 0) is None
    print("PASS: Zero incremental effect")

    results = diagnostic_classification(
        population=1000,
        prevalence=0.10,
        sensitivity=0.90,
        specificity=0.80
    )

    assert round(results["true_positives"], 8) == 90
    assert round(results["false_negatives"], 8) == 10
    assert round(results["true_negatives"], 8) == 720
    assert round(results["false_positives"], 8) == 180
    print("PASS: Diagnostic classification")

    try:
        total_cost(-10, 100)
    except ValueError:
        print("PASS: Negative cost rejected")
    else:
        raise AssertionError("Negative cost was not rejected.")

    try:
        cost_per_person(1000, 0)
    except ValueError:
        print("PASS: Zero population rejected")
    else:
        raise AssertionError("Zero population was not rejected.")

    try:
        diagnostic_classification(1000, 1.2, 0.9, 0.8)
    except ValueError:
        print("PASS: Invalid prevalence rejected")
    else:
        raise AssertionError("Invalid prevalence was not rejected.")

    print()
    print("SUCCESS: All 10 checks passed.")
    print("These tests do not establish real-world NHS cost-effectiveness.")


if __name__ == "__main__":
    run_tests()
