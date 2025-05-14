import cv2
from google.colab import files
import matplotlib.pyplot as plt
import numpy as np

# Upload an image file using Google Colab's file upload feature
uploaded = files.upload()

# Read the uploaded image
image_path = list(uploaded.keys())[0]
original_image = cv2.imread(image_path)

# Resize image to 256x256
resized_image = cv2.resize(original_image, (256, 256))


# (a) Translation
translation_matrix = np.float32([[1, 0, 50], [0, 1, 50]]) # Translate by (50, 50)
translated_image = cv2.warpAffine(resized_image, translation_matrix, (256, 256))

# (b) Scaling
scaling_matrix = np.float32([[0.5, 0, 0], [0, 0.5, 0]]) # Scale by 0.5
scaled_image = cv2.warpAffine(resized_image, scaling_matrix, (256, 256))

# (c) Rotation
rotation_matrix = cv2.getRotationMatrix2D((128, 128), 45, 1) # Rotate by 45 degrees
rotated_image = cv2.warpAffine(resized_image, rotation_matrix, (256, 256))

# (d) Shrinking
shrink_matrix = np.float32([[0.8, 0, 0], [0, 0.8, 0]]) # Shrink by 20%
shrunk_image = cv2.warpAffine(resized_image, shrink_matrix, (256, 256))

# (e) Zooming
zoom_matrix = np.float32([[1.2, 0, 0], [0, 1.2, 0]]) # Zoom by 20%
zoomed_image = cv2.warpAffine(resized_image, zoom_matrix, (256, 256))

# Display the images

plt.figure(figsize=(15, 5))

plt.subplot(2, 3, 1), plt.imshow(translated_image[:, :, ::-1]), plt.title('Translation')

plt.subplot(2, 3, 2), plt.imshow(scaled_image[:, :, ::-1]), plt.title('Scaling')

plt.subplot(2, 3, 3), plt.imshow(rotated_image[:, :, ::-1]), plt.title('Rotation')

plt.subplot(2, 3, 4), plt.imshow(shrunk_image[:, :, ::-1]), plt.title('Shrinking')

plt.subplot(2, 3, 5), plt.imshow(zoomed_image[:, :, ::-1]), plt.title('Zooming')

plt.subplot(2, 3, 6), plt.imshow(resized_image[:, :, ::-1]), plt.title('Original Image')

plt.show()