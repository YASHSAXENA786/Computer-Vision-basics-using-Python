import cv2
from google.colab import files
import matplotlib.pyplot as plt

# Upload an image file using Google Colab's file upload feature
uploaded = files.upload()

# Read the uploaded image
image_path = list(uploaded.keys())[0]
original_image = cv2.imread(image_path)

# Resize image to 256x256
resized_image = cv2.resize(original_image, (256, 256))
# Assuming 'resized_image' from the previous code block

# Convert the image to grayscale
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Apply contrast stretching
min_val, max_val, _, _ = cv2.minMaxLoc(gray_image)

contrast_stretched = cv2.convertScaleAbs(gray_image, alpha=255.0/(max_val-min_val), beta=-min_val*255.0/(max_val-min_val))

# Compute and plot histograms
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1), plt.imshow(contrast_stretched, cmap='gray'), plt.title('Contrast Stretched Image')

plt.subplot(1, 3, 2), plt.hist(gray_image.ravel(), bins=256, color='black', alpha=0.7, rwidth=0.8)
plt.title('Histogram')

plt.subplot(1, 3, 3), plt.hist(contrast_stretched.ravel(), bins=256, color='black', alpha=0.7, rwidth=0.8)
plt.title('Stretched Histogram')

plt.show()