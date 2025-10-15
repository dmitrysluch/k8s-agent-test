import sympy as sp

def solve_equation(equation_str):
    """
    Solve various types of equations using sympy.
    Handles linear, quadratic, and simple algebraic equations.
    """
    # Parse the equation string
    if '=' in equation_str:
        left, right = equation_str.split('=')
        expr = sp.sympify(f"({left}) - ({right})".replace('^', '**'))
    else:
        # If no equals sign, assume expression = 0
        expr = sp.sympify(equation_str.replace('^', '**'))
    
    # Get variables in the expression
    variables = list(expr.free_symbols)
    
    if len(variables) == 0:
        return "No variables found in equation"
    
    if len(variables) == 1:
        # Single variable equation
        var = variables[0]
        solutions = sp.solve(expr, var)
        
        if len(solutions) == 0:
            return f"No solution found for {var}"
        elif len(solutions) == 1:
            return f"{var} = {solutions[0]}"
        else:
            return f"{var} = {', '.join(map(str, solutions))}"
    else:
        # Multiple variables - return simplified form
        return f"Simplified: {sp.simplify(expr)} = 0"

def solve_system(equations_str):
    """
    Solve system of equations.
    Input: list of equation strings
    """
    equations = []
    symbols = set()
    
    for eq_str in equations_str:
        if '=' in eq_str:
            left, right = eq_str.split('=')
            expr = sp.sympify(f"({left}) - ({right})".replace('^', '**'))
        else:
            expr = sp.sympify(eq_str.replace('^', '**'))
        equations.append(expr)
        symbols.update(expr.free_symbols)
    
    if len(symbols) != len(equations):
        return "Number of equations must match number of variables"
    
    solutions = sp.solve(equations, list(symbols))
    return solutions

def factor_expression(expression):
    """
    Factor a polynomial expression.
    """
    expr = sp.sympify(expression.replace('^', '**'))
    factored = sp.factor(expr)
    return str(factored)
