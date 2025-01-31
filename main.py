import numpy as np
import imageio
import cv2
from scipy.ndimage import gaussian_filter

# Prompt user to enter image path
img = input("Enter the image file path: ")

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def dodge(front, back):
    final_sketch = front * 255 / (255 * back + 1e-6)  # Avoid division by zero
    final_sketch[final_sketch > 255] = 255
    return final_sketch.astype('uint8')

# Read the input image
try:
    ss = imageio.imread(img)
    gray_image = rgb2gray(ss)

    i = 255 * gray_image
    blur = gaussian_filter(i, sigma=15)

    r = dodge(blur, gray_image)

    output_file = "convert_image.png"
    cv2.imwrite(output_file, r)
    
    print(f"Image successfully converted and saved as {output_file}")

except FileNotFoundError:
    print("Error: File not found. Please check the file path and try again.")
except Exception as e:
    print(f"An error occurred: {e}")
