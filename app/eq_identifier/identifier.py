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
    print("parsing")
    text = image_to_string(Image.open(path))
    print("Identified = ", text)
    text = re.sub(r'(\d)([a-zA-z])',r'\1*\2',text)
    print("Replace1 = ", text)

    text = re.sub(r'([a-zA-Z])', r'1*\1',text)
    print("Replace2 = ", text)
    
    lhs, rhs = text.split('=')
    lhs += ' -' + rhs
    print("lhs ", lhs)

    x,y=sp.symbols('x,y')
    expr = parse_expr(lhs)
    print(expr)

    '''
        -if image has caps X it fucks up and coeff is  0 
        - if eq is of type 3x +4  = 10 ,  breaks
        
    '''
    x = float(expr.coeff('X'))
    y = float(expr.coeff('y'))
    c = float(expr.args[0])
    print(x,y,c)
    return {"equation" :{"x_coeff": x or y, "rhs": c*-1, "x_expo":1} ,"text": lhs  ,'type':"simple"}

def identify(paths):
    print(paths ,"paths = ")
    if len(paths) == 1:
        eq = parse(paths[0])
        print(eq)
        return eq
    
    else:
        #mutliple images for simultaneous
        '''
        
        '''
        
        return { "type" : "simultaneous", 
                 "equation" : {
                    "equation_a" : {
                        "x_coeff" :1 , 
                        "y_coeff":  1,
                        "rhs":1,
                        },

                    "equation_b" : {
                        "x_coeff" :1 , 
                        "y_coeff":  1,
                        "rhs":1
                        }
                    }
                }

        
            

    
