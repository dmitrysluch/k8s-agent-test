from flask import Flask, render_template, request, jsonify
import math
import sympy as sp
from modules.calculator import evaluate_expression
from modules.plotter import generate_plot
from modules.solver import solve_equation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compute', methods=['POST'])
def compute():
    query = request.json.get('query', '')
    result = process_query(query)
    return jsonify(result)

def process_query(query):
    try:
        # Try to evaluate as mathematical expression
        numeric_result = evaluate_expression(query)
        return {
            'type': 'numeric',
            'result': numeric_result,
            'latex': f"${sp.latex(sp.sympify(query))} = {numeric_result}$"
        }
    except:
        try:
            # Try to solve equation
            solution = solve_equation(query)
            return {
                'type': 'equation',
                'result': solution,
                'latex': f"${sp.latex(sp.sympify(query))} \\Rightarrow {sp.latex(solution)}$"
            }
        except:
            return {
                'type': 'error',
                'result': 'Could not process query',
                'latex': ''
            }

if __name__ == '__main__':
    app.run(debug=True)
