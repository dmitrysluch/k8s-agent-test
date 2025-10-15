# Wolfram Alpha Clone

A Python Flask-based mathematical computation engine that mimics Wolfram Alpha functionality.

## Features

- **Mathematical Expression Evaluation**: Compute arithmetic expressions, polynomials, and functions
- **Equation Solving**: Solve linear and quadratic equations
- **Symbolic Computation**: Differentiation and integration using SymPy
- **Function Plotting**: Generate plots of mathematical functions
- **MathJax Rendering**: Beautiful mathematical formula rendering in the frontend

## Project Structure

```
wolfram_app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── modules/              # Core computation modules
│   ├── calculator.py     # Expression evaluation
│   ├── solver.py         # Equation solving
│   └── plotter.py        # Function plotting
└── templates/
    └── index.html        # Frontend with MathJax
```

## Installation

1. Clone or navigate to the project directory:
   ```bash
   cd /workspace/wolfram_app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python3 app.py
   ```

4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Usage Examples

- **Basic Arithmetic**: `2+2*3`
- **Polynomials**: `x^2 + 2*x + 1`
- **Equations**: `x^2 - 4 = 0`
- **Trigonometric**: `sin(x) + cos(x)`
- **Differentiation**: `diff(x^2, x)`
- **Integration**: `integrate(x^2, x)`

## Dependencies

- **Flask**: Web framework
- **SymPy**: Symbolic mathematics
- **NumPy**: Numerical computations
- **Matplotlib**: Plotting and visualization
- **MathJax**: Frontend mathematical rendering

## API Endpoints

- `GET /`: Main interface
- `POST /compute`: Compute mathematical queries

## Modules

### Calculator Module
- `evaluate_expression()`: Evaluate mathematical expressions
- `differentiate()`: Compute derivatives
- `integrate()`: Compute integrals

### Solver Module
- `solve_equation()`: Solve single-variable equations
- `solve_system()`: Solve systems of equations
- `factor_expression()`: Factor polynomials

### Plotter Module
- `generate_plot()`: Create function plots
- `plot_multiple_functions()`: Plot multiple functions

## License

This project is for educational purposes.
