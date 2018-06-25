from flask import Blueprint, request, render_template

from app.ext import images

upload_blue = Blueprint('upload', __name__)

@upload_blue.route('/img/', methods=['GET','POST'])
def upload_img():
    if request.method == 'POST':
        images.save(request.files['img'])
        return '111'
    elif request.method == 'GET':
        return render_template('upload.html')