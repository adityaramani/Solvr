from flask import Flask
from app.eq_solver.controller import eq_solver as solver_mod
from app.view.controller import view as view_mod

app = Flask(__name__, template_folder='templates')
app.config.from_object('config')

app.register_blueprint(solver_mod)
app.register_blueprint(view_mod)

app.run(host='0.0.0.0', port=8080, debug=True)
