# Test script for Wolfram Alpha modules

from modules.calculator import evaluate_expression, differentiate, integrate
from modules.solver import solve_equation, factor_expression
from modules.plotter import generate_plot

def test_calculator():
    print("Testing Calculator Module:")
    print(f"2+2*3 = {evaluate_expression('2+2*3')}")
    print(f"x^2 + 2*x + 1 = {evaluate_expression('x^2 + 2*x + 1')}")
    print(f"diff(x^2, x) = {differentiate('x^2', 'x')}")
    print(f"integrate(x^2, x) = {integrate('x^2', 'x')}")
    print()

def test_solver():
    print("Testing Solver Module:")
    print(f"x^2 - 4 = 0: {solve_equation('x^2 - 4 = 0')}")
    print(f"x^2 + 2*x + 1 = 0: {solve_equation('x^2 + 2*x + 1 = 0')}")
    print(f"factor(x^2 - 4): {factor_expression('x^2 - 4')}")
    print()

def test_plotter():
    print("Testing Plotter Module:")
    plot_result = generate_plot('x^2', (-5, 5))
    if plot_result.startswith('data:image/png;base64,'):
        print("Plot generation successful (base64 image generated)")
    else:
        print(f"Plot generation failed: {plot_result}")
    print()

if __name__ == "__main__":
    test_calculator()
    test_solver()
    test_plotter()
    print("All tests completed!")
