import cv2
import numpy as np
from google.colab import files
import matplotlib.pyplot as plt
#function to sharpen an image
def sharpen_image(image):
  gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
  gradient_x=cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)
  gradient_y=cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)
  gradient_magnitude=np.sqrt(gradient_x**2+gradient_y**2)
  sharpened_image=cv2.addWeighted(image,1.5,cv2.cvtColor(gradient_magnitude.astype(np.uint8),cv2.COLOR_GRAY2BGR),-0.5,0)
  return sharpened_image
uploaded=files.upload()

image_path=list(uploaded.keys())[0]
image=cv2.imread(image_path)

image=cv2.resize(image,(256,256))
sharpened_image=sharpen_image(image)

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(sharpened_image,cv2.COLOR_BGR2RGB))
plt.title('Sharpened Image')
plt.show()