# Image Caption Generator

Welcome to the **Image Caption Generator**! This is a complete web application built with Python (Flask) that uses the Hugging Face BLIP model to automatically generate descriptive captions for your images.

## Features
- **Upload Image:** Users can upload an image using a modern, user-friendly interface.
- **Preview Image:** See a preview of the image you just uploaded before generating a caption.
- **Generate Captions:** Powered by the Hugging Face BLIP model, the app generates an accurate caption for the uploaded image instantly.
- **Clean UI:** Styled with a responsive and interactive design (HTML, CSS, JS).

## Technologies Used
- **Backend:** Python, Flask
- **Machine Learning Model:** Hugging Face BLIP (Bootstrapping Language-Image Pre-training)
- **Frontend:** HTML5, CSS3, Vanilla JavaScript

## Project Structure
```
image-caption/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies (make sure to create this if you haven't yet)
├── README.md              # Project documentation
│
├── static/                
│   ├── style.css          # Styling for the web app
│   └── script.js          # JavaScript for frontend interactions
│
├── templates/             
│   └── index.html         # Main HTML page
│
├── uploads/               # Directory where uploaded images are saved temporarily
└── sample_images/         # Images used for testing
```

## How to Run the App Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Madhulatha18/Dl_imagecaptiongenerator_Techtitans.git
   ```

2. **Navigate into the project directory:**
   ```bash
   cd Dl_imagecaptiongenerator_Techtitans
   ```

3. **Install the required dependencies:**
   *(Ensure you have Python installed on your system)*
   ```bash
   pip install flask transformers torch Pillow
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Open your browser:**
   Go to `http://127.0.0.1:5000/` to test it out!

## License
Feel free to use and modify!
