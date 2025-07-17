# Computer Vision Toolkit – Python & OpenCV

A collection of basic Computer Vision algorithms implemented in Python using OpenCV.  
This toolkit includes modules for image transformations, noise simulation & reduction, histogram analysis, and more.

---

## 🛠️ Features
- Image transformations (scaling, rotation, translation)
- Noise simulation (Gaussian, Salt & Pepper)
- Noise reduction (Median Filter, Gaussian Blur, Bilateral Filter)
- Histogram analysis & visualization
- Image enhancement utilities

---

## 📑 API Overview

### Noise Simulation & Reduction

#### `add_gaussian_noise(image, mean=0, sigma=10)`
> Adds Gaussian noise to the input image.

- **Params:**
  - `image` *(np.ndarray)* – Input image
  - `mean` *(int)* – Mean of Gaussian noise (default = 0)
  - `sigma` *(int)* – Standard deviation of noise (default = 10)
- **Returns:** Noisy image *(np.ndarray)*


#### `apply_median_filter(image, kernel_size=3)`
> Reduces noise in an image using a median filter.

- **Params:**
  - `image` *(np.ndarray)* – Input noisy image
  - `kernel_size` *(int)* – Filter size (default = 3)
- **Returns:** Denoised image *(np.ndarray)*


---

### Histogram Analysis

#### `plot_histogram(image, title='Histogram')`
> Plots the histogram of pixel intensities for grayscale or color images.

- **Params:**
  - `image` *(np.ndarray)* – Input image
  - `title` *(str)* – Plot title (default = 'Histogram')
- **Returns:** Displays histogram plot


#### `equalize_histogram(image)`
> Applies histogram equalization for contrast enhancement (grayscale only).

- **Params:**
  - `image` *(np.ndarray)* – Grayscale input image
- **Returns:** Contrast-enhanced image *(np.ndarray)*


---

## 📂 How to Use

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
```

2. Install dependencies:
```bash
pip install opencv-python matplotlib numpy
```

3. Import and use in your Python scripts:
```python
from cv_toolkit import add_gaussian_noise, apply_median_filter, plot_histogram
```

---

## 📝 Example Notebooks
> Check the `examples/` folder for usage examples and visual outputs.

---

## 🗂️ Project Structure

```
cv_toolkit/
│
├── cv_toolkit/
│   ├── __init__.py
│   ├── noise.py
│   ├── histogram.py
│   └── transformations.py
├── examples/
│   └── demo_notebook.ipynb
├── README.md
├── requirements.txt
└── LICENSE
```

---

## 🖋️ License  
This project is open-source and available under the [MIT License](LICENSE).

