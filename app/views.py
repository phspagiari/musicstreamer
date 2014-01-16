import os
from flask import render_template, request, send_from_directory
from werkzeug.utils import secure_filename
from app import app

musicpath = str(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		file = request.files['file']
		if file.filename:
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return render_template('index.html', filename=filename)
	return render_template('index.html')

@app.route('/load/<filename>')
def load(filename):
	return render_template('index.html', filename=filename)

@app.route('/list')
def list():
	filelist = [ f for f in os.listdir(str(app.config['UPLOAD_FOLDER'])) if os.path.isfile(os.path.join(str(app.config['UPLOAD_FOLDER']),f)) ]
	return render_template('index.html', filelist=filelist)
