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

def parse(path):
    text = image_to_string(Image.open(path))
    text = re.sub(r'(\d)([a-zA-z])',r'\1*\2',text)
    text = re.sub(r'([a-zA-Z])', r'1*\1',text)
    lhs, rhs = text.split('=')
    lhs += ' -' + rhs
    x,y=sp.symbols('x,y')
    expr = parse_expr(lhs)
    return expr

def identify(paths):
    
    if len(paths) == 1:
        expr = parse(paths[0])
        x = float(expr.coeff(x))
        y = float(expr.coeff(y))
        c = float(expr.args[0])
        return {"x_coeff": x or y, "rhs": c*-1, "x_expo":1 ,  'types':"simple"}
    
    else:
        #mutliple images
        
        return { "type" : "simultaneous", 
                 "equation" : {
                    "equation_a" : {
                        "x_coeff" : , 
                        "y_coeff":  .
                        "rhs":,
                        },

                    "equation_b" : {
                        "x_coeff" : , 
                        "y_coeff":  ,
                        "rhs":
                        }
                    }
                }

        
            

    
