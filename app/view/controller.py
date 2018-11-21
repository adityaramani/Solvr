from flask import Blueprint, request,flash, jsonify, render_template,redirect, url_for
from werkzeug.utils import  secure_filename
import os
import app.eq_identifier.identifier as eq_identifier  

view = Blueprint('view_render', __name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
@view.route("/", methods= ['GET'])
def index():
    return render_template('index.html')

@view.route("/image/upload", methods=['POST'])
def file_upload():
    if request.method == 'POST':
        print("GOT REQUEST")
        for i in request.files:
            print(i, request.files[i])        
        
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['image']

        if file.filename == '':
            flash('No selected file')
            return "ERROR"

        if file:
            filename = secure_filename(file.filename)
            path  = os.path.join("app/static/image_upload", filename)
            file.save(path)
            eq = eq_identifier.identify(path)
            return "Success"

    return "Success"