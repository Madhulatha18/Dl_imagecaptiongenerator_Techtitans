import os
from flask import Flask, request, jsonify, render_template
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load BLIP model and processor
print("Loading model...")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
print("Model loaded.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload-image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        raw_image = Image.open(filepath).convert('RGB')
        
        # conditional image captioning
        inputs = processor(raw_image, return_tensors="pt")
        out = model.generate(**inputs)
        caption = processor.decode(out[0], skip_special_tokens=True)
        
        return jsonify({'caption': caption})

import webbrowser
from threading import Timer

if __name__ == '__main__':
    # Function to open the browser
    def open_browser():
        webbrowser.open_new("http://127.0.0.1:5000")
        
    # Wait 1.5 seconds for the server to start, then open the browser
    Timer(1.5, open_browser).start()
    
    # Start the Flask app
    print("\n" + "="*50)
    print("🚀 Server is ready! Opening your beautifully crafted app...")
    print("👉 If it doesn't open automatically, click here: http://127.0.0.1:5000")
    print("="*50 + "\n")
    
    app.run(debug=True, port=5000, use_reloader=False)
