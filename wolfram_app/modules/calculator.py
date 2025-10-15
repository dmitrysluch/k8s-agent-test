import math
import sympy as sp
import numpy as np

def evaluate_expression(expression):
    """
    Evaluate mathematical expressions using sympy for symbolic computation
    and numpy for numerical functions.
    """
    # Replace common mathematical functions with sympy equivalents
    expr = expression.replace('^', '**')
    
    # Parse and evaluate the expression
    parsed_expr = sp.sympify(expr)
    
    # If it's a simple numeric expression, evaluate numerically
    if parsed_expr.is_number:
        return float(parsed_expr.evalf())
    else:
        # For symbolic expressions, return the simplified form
        return str(parsed_expr.simplify())

def evaluate_function(func_str, x_value):
    """
    Evaluate a function at a specific x value.
    Example: "x^2 + 2*x + 1" at x=3
    """
    x = sp.Symbol('x')
    func = sp.sympify(func_str.replace('^', '**'))
    return float(func.subs(x, x_value).evalf())

def differentiate(expression, variable='x'):
    """
    Differentiate an expression with respect to a variable.
    """
    var = sp.Symbol(variable)
    expr = sp.sympify(expression.replace('^', '**'))
    derivative = sp.diff(expr, var)
    return str(derivative)

def integrate(expression, variable='x'):
    """
    Integrate an expression with respect to a variable.
    """
    var = sp.Symbol(variable)
    expr = sp.sympify(expression.replace('^', '**'))
    integral = sp.integrate(expr, var)
    return str(integral)
