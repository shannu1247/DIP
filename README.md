# 📸 Digital Image Processing Experiments in MATLAB

This repository contains basic digital image processing experiments implemented in MATLAB using the test image `lena.jpg`. These scripts demonstrate fundamental operations such as grayscale conversion, color channel separation, and binary thresholding.

---

## 🧪 Experiments Overview

### 🔬 Experiment 1: RGB to Grayscale Conversion
**File:** `experiment1_rgb_to_grayscale.m`

- Reads a color image (`lena.jpg`)
- Converts it to grayscale using MATLAB’s built-in `rgb2gray()` function
- Displays original and grayscale images side by side

📷 **Output:**
- Left: Original RGB image
- Right: Grayscale version

---

### 🎨 Experiment 2: RGB Channel Separation
**File:** `experiment2_rgb_channel_separation.m`

- Reads `lena.jpg`
- Separates Red, Green, and Blue components
- Sets other channels to zero to isolate each primary color
- Displays the original image and all three channels in a 2×2 grid

📷 **Output:**
- Top-left: Original image  
- Top-right: Red channel  
- Bottom-left: Green channel  
- Bottom-right: Blue channel

---

### ⚫⚪ Experiment 3: Manual Thresholding (Grayscale to Binary)
**File:** `experiment3_manual_thresholding.m`

- Converts RGB image to grayscale manually by averaging R, G, B channels
- Calculates the **mean intensity** of the grayscale image
- Applies a threshold:  
  - Pixels > mean → white (255)  
  - Pixels ≤ mean → black (0)
- Displays the resulting black and white image

📷 **Output:** A binary image clearly showing regions based on brightness.

---

## 🖼️ Test Image Used

All experiments use:
- **`lena.jpg`** — a standard test image used in DIP.

Make sure `lena.jpg` is in the **same directory** as your `.m` files before running.

---

## 💻 How to Run

Open MATLAB and make sure the current directory contains the script files and `lena.jpg`. Then run:

```matlab
run('experiment1_rgb_to_grayscale.m')
