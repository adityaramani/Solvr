from flask import Blueprint, request, jsonify
from app.eq_solver.models import *

eq_solver = Blueprint('solver', __name__, url_prefix='/solve')

@eq_solver.route('/simple',methods=['POST'])
def solve_simple_equation():
    print("Got request")
    print(request.json)
    args = request.json['equation']
    eq = Simple(**args)
    eq.solve()
    solution =  eq.solution
    return jsonify(solution)


@eq_solver.route('/simultaneous',methods=['POST'])
def solve_simul_equation():
    print("Got request")
    print(request.json)
    args_a = request.json['equation']['equation_a']
    args_b = request.json['equation']['equation_b']

    eq_a = Simultaneous(**args_a)
    eq_b = Simultaneous(**args_b)
    eq_a.solve(eq_b)

    solution =  eq_a.solution
    return jsonify(solution)


@eq_solver.route('/quadratic',methods=['POST'])
def solve_quad_equation():
    print("Got request")
    print(request.json)
    args = request.json['equation']

    eq_a = Quadratic(**args)
    eq_a.solve()

    solution =  eq_a.solution
    return jsonify(solution)