import re

# Read the current app.py
with open('app.py', 'r') as f:
    content = f.read()

# Replace the process_query function with a fixed version
new_process_query = '''def process_query(query):
    try:
        # Try to evaluate as mathematical expression
        numeric_result = evaluate_expression(query)
        return {
            'type': 'numeric',
            'result': numeric_result,
            'latex': f"${sp.latex(sp.sympify(query.replace('^', '**')))} = {numeric_result}$"
        }
    except:
        try:
            # Try to solve equation
            solution = solve_equation(query)
            # Fix LaTeX for equations with equals signs
            if '=' in query:
                left, right = query.split('=')
                left_expr = sp.sympify(left.replace('^', '**'))
                right_expr = sp.sympify(right.replace('^', '**'))
                latex_str = f"${sp.latex(left_expr)} = {sp.latex(right_expr)} \\Rightarrow {solution}$"
            else:
                latex_str = f"${sp.latex(sp.sympify(query.replace('^', '**')))} \\Rightarrow {solution}$"
            return {
                'type': 'equation',
                'result': solution,
                'latex': latex_str
            }
        except Exception as e:
            return {
                'type': 'error',
                'result': f'Could not process query: {str(e)}',
                'latex': ''
            }'''

# Replace the old process_query function
pattern = r'def process_query\(query\):.*?return \{.*?\}.*?\}'
new_content = re.sub(pattern, new_process_query, content, flags=re.DOTALL)

# Write the fixed content back
with open('app.py', 'w') as f:
    f.write(new_content)

print('app.py fixed successfully')
