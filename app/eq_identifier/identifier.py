"""
Find the equation from an image and return its type and coefficient.
"""


from PIL import Image
from pytesseract import image_to_string
import json
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
import re

###################################################################
# This function parses simple equation in one variable.
def parse(text):
    actualText = text
    print("Identified = ", text)
    text = re.sub(r'(\d)([a-zA-z])',r'\1*\2',text)
    print("Replace1 = ", text)

    text = re.sub(r'([a-zA-Z])', r'1*\1',text)
    print("Replace2 = ", text)

    text = text.replace('X', 'x')
    text = text.replace('Y','y')
    print("Replace3 = ", text)  
    
    lhs, rhs = text.split('=')
    lhs += ' -' + rhs
    print("lhs ", lhs)

    x,y=sp.symbols('x,y')
    expr = parse_expr(lhs)
    print(expr)

   
    x = float(expr.coeff(x))
    y = float(expr.coeff(y))
    c = float(expr.args[0])
    print(x,y,c)
    print("#############################################################################")
    return {"equation" :{"x_coeff": x or y, "rhs": c*-1, "x_expo":1} ,"text": actualText  ,'type':"simple"}

#############################################################################

#This eqauation parses simultaneous eqaution in 2 variables. JSON is different in 2 functions
def parseSimultaneous(text):
    actualText = text
    print("Identified = ", text)
    text = re.sub(r'(\d)([a-zA-z])',r'\1*\2',text)
    print("Replace1 = ", text)

    text = re.sub(r'([a-zA-Z])', r'1*\1',text)
    print("Replace2 = ", text)

    text = text.replace('X', 'x')
    text = text.replace('Y','y')
    print("Replace3 = ", text)  
    
    lhs, rhs = text.split('=')
    lhs += ' -' + rhs
    print("lhs ", lhs)

    x,y=sp.symbols('x,y')
    expr = parse_expr(lhs)
    print(expr)

    
    x = float(expr.coeff(x))
    y = float(expr.coeff(y))
    c = float(expr.args[0])
    print(x,y,c)
    print("############################################################")
    return {"equation" :{"x_coeff": x, "y_coeff": y, "rhs": c*-1, "x_expo":1} ,"text": actualText}

#########################################################################
#This is the main function to find if its simultaneous or simple and parse accordingly.

def identify(path):
    print("parsing")
    text = image_to_string(Image.open(path))
    #print(text)

    if('\n' not in text):
        return(parse(text))
    else:
        #mutliple images for simultaneous
        text1, text2 = re.sub('\n+',',',text).split(',')
        
        eq1Output = parseSimultaneous(text1)
        eq2Output = parseSimultaneous(text2)
               
        return { "type" : "simultaneous", 
                 "equation" : {
                    "equation_a" : {
                        "x_coeff" : eq1Output['equation']['x_coeff'] , 
                        "y_coeff":  eq1Output['equation']['y_coeff'],
                        "rhs": eq1Output['equation']['rhs'],
                        "text": eq1Output['text']
                        },

                    "equation_b" : {
                        "x_coeff" : eq2Output['equation']['x_coeff'], 
                        "y_coeff":  eq2Output['equation']['y_coeff'],
                        "rhs": eq2Output['equation']['rhs'],
                        "text": eq2Output['text']
                        }
                    }
                }

        
            

    
