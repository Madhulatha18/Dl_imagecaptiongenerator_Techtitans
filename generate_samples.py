import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs('sample_images', exist_ok=True)

# Define some colors and text
samples = [
    ("sample_images/image1.jpg", (255, 100, 100), "A red square"),
    ("sample_images/image2.jpg", (100, 255, 100), "A green square"),
    ("sample_images/image3.jpg", (100, 100, 255), "A blue square")
]

for filepath, color, text in samples:
    img = Image.new('RGB', (400, 400), color=color)
    d = ImageDraw.Draw(img)
    # Just draw a simple cross to give it some feature
    d.line([(0, 0), (400, 400)], fill=(0, 0, 0), width=5)
    d.line([(0, 400), (400, 0)], fill=(0, 0, 0), width=5)
    img.save(filepath)

print("Sample images generated successfully.")
