from flask import Flask, request, jsonify, render_template, send_from_directory
import os
from werkzeug.utils import secure_filename
from datetime import datetime
import random

app = Flask(__name__)

# Configurations
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# In-memory storage for posts
posts = []

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/add_post', methods=['POST'])
def add_post():
    data = request.form
    text = data.get('text', '')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    print("Received data:", data)  # Log the data received
    print("Latitude:", latitude, "Longitude:", longitude)

    image_url = None
    if 'image' in request.files:
        file = request.files['image']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            image_url = f"/uploads/{filename}"

    post = {
        "id": random.randint(1000, 9999),
        "text": text,
        "latitude": latitude,
        "longitude": longitude,
        "image_url": image_url,
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    posts.append(post)

    return jsonify({"message": "Post added successfully", "post": post}), 201

# Route to serve uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/get_posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

if __name__ == '__main__':
    app.run(debug=True)