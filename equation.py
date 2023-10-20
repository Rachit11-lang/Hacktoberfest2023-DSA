from sympy import symbols, Eq, solve

# Define the symbolic variable
x = symbols('x')

# Define the equation: 2x + 5 = 13
equation = Eq(2*x + 5, 13)

# Solve the equation symbolically
solutions = solve(equation, x)

# Print the solution
print("The solution for x is:", solutions)
