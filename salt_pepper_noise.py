import cv2
import matplotlib.pyplot as plt
from google.colab import files
import numpy as np

# Upload image
uploaded = files.upload()
image_path = list(uploaded.keys())[0]
image = cv2.imread(image_path)  # Load in grayscale

def add_salt_and_pepper_noise(image, salt_prob=0.02, pepper_prob=0.02):
    """
    Add salt and pepper noise to an image.

    :param image: Input image (NumPy array).
    :param salt_prob: Probability of salt noise (white pixels).
    :param pepper_prob: Probability of pepper noise (black pixels).
    :return: Noisy image.
    """
    noisy_image = image.copy()
    total_pixels = image.size  # Total number of pixels

    # Add salt noise (white pixels)
    num_salt = int(total_pixels * salt_prob)
    salt_coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape[:2]]
    noisy_image[salt_coords[0], salt_coords[1]] = 255

    # Add pepper noise (black pixels)
    num_pepper = int(total_pixels * pepper_prob)
    pepper_coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape[:2]]
    noisy_image[pepper_coords[0], pepper_coords[1]] = 0

    return noisy_image

# Apply salt and pepper noise
noisy_image = add_salt_and_pepper_noise(image, salt_prob=0.02, pepper_prob=0.02)

# Plot images
plt.figure(figsize=(10, 5))

# Original Image
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis("off")

# Noisy Image
plt.subplot(1, 2, 2)
plt.imshow(noisy_image)
plt.title("Noisy Image")
plt.axis("off")

plt.show()
