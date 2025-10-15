import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import io
import base64

def generate_plot(expression, x_range=(-10, 10), points=1000):
    """
    Generate a plot of a mathematical function.
    Returns base64 encoded image string.
    """
    try:
        # Parse the expression
        x = sp.Symbol('x')
        expr = sp.sympify(expression.replace('^', '**'))
        
        # Convert to numpy function
        func = sp.lambdify(x, expr, 'numpy')
        
        # Generate x values
        x_vals = np.linspace(x_range[0], x_range[1], points)
        y_vals = func(x_vals)
        
        # Create plot
        plt.figure(figsize=(10, 6))
        plt.plot(x_vals, y_vals, 'b-', linewidth=2)
        plt.grid(True, alpha=0.3)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title(f'Plot of $f(x) = {sp.latex(expr)}$')
        
        # Convert to base64 string
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode()
        plt.close()
        
        return f"data:image/png;base64,{image_base64}"
        
    except Exception as e:
        return f"Error generating plot: {str(e)}"

def plot_multiple_functions(expressions, x_range=(-10, 10), points=1000):
    """
    Plot multiple functions on the same graph.
    """
    try:
        plt.figure(figsize=(10, 6))
        x = sp.Symbol('x')
        x_vals = np.linspace(x_range[0], x_range[1], points)
        
        colors = ['b-', 'r-', 'g-', 'c-', 'm-', 'y-', 'k-']
        
        for i, expr_str in enumerate(expressions):
            expr = sp.sympify(expr_str.replace('^', '**'))
            func = sp.lambdify(x, expr, 'numpy')
            y_vals = func(x_vals)
            plt.plot(x_vals, y_vals, colors[i % len(colors)], 
                    linewidth=2, label=f'$f_{i+1}(x) = {sp.latex(expr)}$')
        
        plt.grid(True, alpha=0.3)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Multiple Function Plot')
        plt.legend()
        
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode()
        plt.close()
        
        return f"data:image/png;base64,{image_base64}"
        
    except Exception as e:
        return f"Error generating plot: {str(e)}"
