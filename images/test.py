from PIL import Image
import os

# Directory to scan (current directory)
directory = os.getcwd()

# Loop over all files in the directory
for filename in os.listdir(directory):
    if filename.lower().endswith(".gif"):
        gif_path = os.path.join(directory, filename)
        
        # Open the GIF
        with Image.open(gif_path) as im:
            # Extract first frame
            first_frame = im.convert("RGBA")
            
            # Save as PNG with the same name (replace .gif with .png)
            png_filename = filename.rsplit(".", 1)[0] + ".png"
            png_path = os.path.join(directory, png_filename)
            first_frame.save(png_path)
            print(f"Converted {filename} → {png_filename}")

print("All GIFs converted to PNG (first frame).")
