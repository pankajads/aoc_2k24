from itertools import product

def evaluate_expression(numbers, operators):
    """
    Evaluate the expression with numbers and operators in left-to-right order.
    Supports +, *, and concatenation (||).
    """
    result = numbers[0]
    for i, operator in enumerate(operators):
        if operator == '+':
            result += numbers[i + 1]
        elif operator == '*':
            result *= numbers[i + 1]
        elif operator == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result

def find_calibration_result(equations, allowed_operators):
    """
    Determine the total calibration result for valid equations.
    Allows dynamic selection of operators.
    """
    total_calibration_result = 0

    for test_value, numbers in equations:
        num_operators = len(numbers) - 1
        found_solution = False

        # Try all combinations of allowed operators
        for operators in product(allowed_operators, repeat=num_operators):
            if evaluate_expression(numbers, operators) == test_value:
                found_solution = True
                break

        if found_solution:
            total_calibration_result += test_value

    return total_calibration_result

# Sample input file
filename = "input_sample.txt"
with open(filename) as filehandler:
    equations = []
    for line in filehandler.readlines():
        test_value, numbers = line.split(':')
        test_value = int(test_value.strip())
        numbers = list(map(int, numbers.strip().split()))
        equations.append((test_value, numbers))

# Calculate results for different operator sets
result1 = find_calibration_result(equations, allowed_operators=['+', '*'])
result2 = find_calibration_result(equations, allowed_operators=['+', '*', '||'])

# Print the results
print(f"Total Calibration Result (with +, *): {result1}")
print(f"Total Calibration Result (with +, *, ||): {result2}")
