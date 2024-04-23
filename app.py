from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__)

# Define the image storage path
IMAGE_DIR = '/images'

# Function to get images in the correct order
def get_images():
    images = sorted([img for img in os.listdir(IMAGE_DIR)])
    return images

# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to get an image URL based on the slider value (timestamp index)
@app.route('/get_image')
def get_image():
    slider_value = int(request.args.get('value'))
    images = get_images()
    # Get the image file name based on slider value
    image_file = images[slider_value]
    # Construct the image URL
    image_url = f'/static/images/{image_file}'
    return jsonify({'image_url': image_url})

if __name__ == '__main__':
    app.run(debug=True)
