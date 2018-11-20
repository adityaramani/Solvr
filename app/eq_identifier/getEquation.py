"""
Find the equation from an image and return its type and coefficient.
"""


from PIL import Image
from pytesseract import image_to_string
import json
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
import re

LINEAR = 0
LINEAR2 = 1
QUAD = 2

def getLhsRhs(path):
    text = image_to_string(Image.open(path))
    text = re.sub(r'(\d)([a-zA-z])',r'\1*\2',text)
    text = re.sub(r'([a-zA-Z])', r'1*\1',text)
    lhs, rhs = text.split('=')
    lhs += ' -' + rhs
    print(lhs)
    x,y=sp.symbols('x,y')
    expr = parse_expr(lhs)
    x = float(expr.coeff(x))
    y = float(expr.coeff(y))
    c = float(expr.args[0])
    if(x == 0 or y == 0):
        return(json.dumps({'lhs':{'x':x,'c':c,'y':y},  'types':LINEAR}))
    else:
        return(json.dumps({'lhs':{'x':x,'c':c,'y':y},  'types':LINEAR2}))

        
            

    
