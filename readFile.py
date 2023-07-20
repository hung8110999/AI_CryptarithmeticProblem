def is_valid_cryptarithmetic_string(s):
    allowed_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    allowed_operators = set("(+-*=)")

    # Function to check if a given expression is valid (contains only allowed characters and operators).
    def is_valid_expression(expression):
        stack = []
        for i, char in enumerate(expression):
            if char in allowed_operators:
                if char == '(':
                    stack.append(char)
                elif char == ')':
                    if not stack or stack[-1] != '(':
                        return False
                    stack.pop()
            elif char not in allowed_characters and char != ' ':
                return False

            # Check for invalid character-parentheses combinations like a)b or a(b)
            if i < len(expression) - 2:
                if expression[i] in allowed_characters and expression[i + 1] == ')' and expression[
                    i + 2] in allowed_characters:
                    return False
                if expression[i] in allowed_characters and expression[i + 1] == '(' and expression[
                    i + 2] in allowed_characters:
                    return False

        return len(stack) == 0  # Check if all parentheses are balanced.

    # Split the input string by "=" to get the left and right parts of the equation.
    parts = s.split("=")

    # Ensure there is exactly one "=" in the string.
    if len(parts) != 2:
        return False

    left_part = parts[0].strip()
    right_part = parts[1].strip()

    # Check if the left and right parts are valid expressions.
    if not is_valid_expression(left_part) or not is_valid_expression(right_part):
        return False

    # Check if the left part has at least one operator and the right part has no operators.
    if all(char not in allowed_operators for char in left_part) or any(
            char in allowed_operators for char in right_part):
        return False

    return True

def readFile():
    input_file = "data.txt"  # Replace "input.txt" with the name of your input file.

    with open(input_file, "r") as file:
        for line in file:
            expression = line.strip()
            if is_valid_cryptarithmetic_string(expression):
                print(f"{expression} is a valid.")
            else:
                print(f"{expression} is NOT a valid.")
    file.close()