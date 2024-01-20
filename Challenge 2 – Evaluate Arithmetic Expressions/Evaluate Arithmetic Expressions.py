import re
import tkinter as tk
from tkinter import filedialog
from sympy import sympify

def evaluate_expression(expression):
    # Replace caret (^) with ** for exponentiation
    expression = expression.replace('^', '**')
    expression = expression.replace(')(', ')*(')
        

    # Evaluate the expression using eval
    result = sympify(expression)

    return result

def solve_arithmetic(file_path):
    # Read input file
    with open(file_path, 'r') as input_file:
        lines = input_file.readlines()

    # Process each line
    results = []
    for line in lines:
        # Remove leading and trailing whitespaces
        line = line.strip()

        # Check if the line is not empty
        if line:
            
            # Extract expression and solve
            expression, equals_sign = re.split(r'\s*=\s*', line)
            result = evaluate_expression(expression)

            # Append result to the results list
            results.append(f"{expression} = {result}\n")

    # Write output to a new file
    output_file_path = 'output.txt'
    with open(output_file_path, 'w') as output_file:
        output_file.writelines(results)

# Example usage:
input_file_path = 'input.txt'
solve_arithmetic(input_file_path)

def Display():
    print()
    print(f"Expressions solved.\nOutput file generated.")
    print()
    # pass
def load_file():
    file_path = filedialog.askopenfilename(title="Select a Text File")
    if file_path:
        print("Input File Path : ",file_path)
        solve_arithmetic(file_path)
        Display()
        return True
        # pass
    else:
        return []

def main():
    words = []
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    words = load_file()

if __name__ == "__main__":
    main()




