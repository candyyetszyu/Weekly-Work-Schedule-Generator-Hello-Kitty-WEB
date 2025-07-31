#!/usr/bin/env python3
"""
Create a Hello Kitty themed background image
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_hello_kitty_background():
    # Create a pink background image
    width, height = 800, 900
    bg_color = (255, 230, 242)  # Light pink
    image = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(image)
    
    # Draw Hello Kitty inspired elements
    # Main circles for Hello Kitty face
    face_color = (255, 255, 255)  # White
    bow_color = (255, 105, 180)   # Hot pink
    
    # Draw Hello Kitty face (simplified)
    # Head
    draw.ellipse([200, 100, 600, 500], fill=face_color, outline=(200, 200, 200), width=3)
    
    # Ears
    draw.ellipse([180, 80, 280, 180], fill=face_color, outline=(200, 200, 200), width=3)
    draw.ellipse([520, 80, 620, 180], fill=face_color, outline=(200, 200, 200), width=3)
    
    # Bow
    draw.ellipse([350, 60, 450, 160], fill=bow_color, outline=(200, 100, 150), width=2)
    draw.ellipse([320, 80, 380, 140], fill=bow_color, outline=(200, 100, 150), width=2)
    draw.ellipse([420, 80, 480, 140], fill=bow_color, outline=(200, 100, 150), width=2)
    
    # Eyes
    draw.ellipse([280, 200, 320, 240], fill=(0, 0, 0), outline=(0, 0, 0), width=2)
    draw.ellipse([480, 200, 520, 240], fill=(0, 0, 0), outline=(0, 0, 0), width=2)
    
    # Nose
    draw.ellipse([390, 280, 410, 300], fill=(255, 182, 193), outline=(200, 150, 150), width=1)
    
    # Whiskers
    whisker_color = (100, 100, 100)
    # Left whiskers
    draw.line([250, 290, 150, 270], fill=whisker_color, width=3)
    draw.line([250, 300, 150, 300], fill=whisker_color, width=3)
    draw.line([250, 310, 150, 330], fill=whisker_color, width=3)
    # Right whiskers
    draw.line([550, 290, 650, 270], fill=whisker_color, width=3)
    draw.line([550, 300, 650, 300], fill=whisker_color, width=3)
    draw.line([550, 310, 650, 330], fill=whisker_color, width=3)
    
    # Add some decorative elements
    # Small hearts
    heart_color = (255, 182, 193)  # Light pink
    for i in range(5):
        x = 50 + i * 150
        y = 600 + (i % 2) * 50
        # Simple heart shape
        draw.ellipse([x, y, x+20, y+20], fill=heart_color)
        draw.ellipse([x+10, y, x+30, y+20], fill=heart_color)
        draw.polygon([x+15, y+20, x, y+10, x+30, y+10], fill=heart_color)
    
    # Add some stars
    star_color = (255, 255, 255)  # White
    for i in range(8):
        x = 100 + i * 80
        y = 700 + (i % 3) * 30
        # Simple star (5-pointed)
        points = []
        for j in range(5):
            angle = j * 72 - 90
            px = x + 15 * (1 if j % 2 == 0 else 0.5) * (1 if angle % 180 == 0 else 0.7)
            py = y + 15 * (1 if j % 2 == 0 else 0.5) * (1 if angle % 180 == 90 else 0.7)
            points.extend([px, py])
        if len(points) >= 6:
            draw.polygon(points, fill=star_color, outline=(200, 200, 200))
    
    # Save the image
    image.save('hello_kitty_bg.png')
    print("✅ Hello Kitty background image created: hello_kitty_bg.png")
    return 'hello_kitty_bg.png'

if __name__ == "__main__":
    create_hello_kitty_background() 