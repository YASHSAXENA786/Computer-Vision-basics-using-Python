import numpy as np
import matplotlib.pyplot as plt
from skimage import io,color,filters

#from google.colab import files
#load image
image_url="https://static.toiimg.com/photo/imgsize-161580,msid-96352420/96352420.jpg"
image=io.imread(image_url)
gray_image=color.rgb2gray(image)

#apply sobel, prewitt, roberts edge detection
edge_sobel=filters.sobel(gray_image)
edge_prewitt=filters.prewitt(gray_image)
edge_roberts=filters.roberts(gray_image)

#display original and edge detected images
plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.imshow(gray_image,cmap="gray")
plt.title('Original Image')
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(edge_sobel,cmap="gray")
plt.title('Sobel Edge Detection')
plt.axis('off')

plt.subplot(2,2,3)
plt.imshow(edge_prewitt,cmap="gray")
plt.title('Prewitt Edge Detection')
plt.axis('off')

plt.subplot(2,2,4)
plt.imshow(edge_roberts,cmap="gray")
plt.title('Roberts Edge Detection')
plt.axis('off')

plt.show()