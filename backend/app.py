# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from utils import extract_text, extract_document_data

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = './uploads'

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Empty file name"}), 400
    
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Extract text and data
    text = extract_text(filepath)
    data = extract_document_data(text)
    
    # Clean up uploaded file
    os.remove(filepath)
    
    return jsonify(data), 200

if __name__ == '__main__':
    app.run(debug=True)
