from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app.eq_solver.models import *

eq_solver = Blueprint('solver', __name__, url_prefix='/solve')

@eq_solver.route('/simple',methods=['POST'])
def solve_simple_equation():
    print("Got request")
    print(request.json)
    args = request.args['equation']
    eq = Simple(args)
    solution = eq.solve().solution
    print(solution)
    return "Success"