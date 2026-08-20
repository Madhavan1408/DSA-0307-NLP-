import re

def parse_fopc(expression):
    expression = expression.strip()
    quantifier_pattern = r'^(ForAll|Exists)\s+(\w+)\s+(.*)$'
    predicate_pattern = r'^(\w+)\((.*)\)$'
    connective_pattern = r'^(.*)\s+(And|Or|Implies)\s+(.*)$'

    q_match = re.match(quantifier_pattern, expression)
    if q_match:
        quantifier, variable, rest = q_match.groups()
        return {'type': 'quantifier', 'quantifier': quantifier, 'variable': variable, 'body': parse_fopc(rest)}

    c_match = re.match(connective_pattern, expression)
    if c_match:
        left, connective, right = c_match.groups()
        return {'type': 'connective', 'connective': connective, 'left': parse_fopc(left.strip()), 'right': parse_fopc(right.strip())}

    p_match = re.match(predicate_pattern, expression)
    if p_match:
        predicate, args = p_match.groups()
        return {'type': 'predicate', 'name': predicate, 'args': [a.strip() for a in args.split(',')]}

    return {'type': 'unknown', 'value': expression}

expressions = [
    "ForAll x Human(x) Implies Mortal(x)",
    "Exists x Student(x) And Smart(x)",
    "Loves(John, Mary)"
]

for expr in expressions:
    print("Expression:", expr)
    print("Parsed:", parse_fopc(expr))
    print("-" * 50)
