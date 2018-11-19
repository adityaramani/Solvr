from flask import Blueprint, request, jsonify, render_template

view = Blueprint('view_render', __name__)

@view.route("/", methods= ['GET'])
def index():
    return render_template('index.html')