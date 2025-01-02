# Motion-Detection
This project is designed to detect motion between two BMP images and save the results as a BMP file. The images are first converted to grayscale, and then pixel differences are analyzed to detect motion.

Features

Read and write BMP image files

Convert images to grayscale

Detect motion between two images

Save results as a new BMP file

Requirements

Python 3.x

Usage

1. Prepare BMP Files

Place two BMP images in the ./sample/ directory:

sample1.bmp

sample2.bmp

2. Run the Code

Run the following command in the terminal:

python motion_detection.py

3. Outputs

After execution, the following files will be generated:

grayscale_frame1.bmp: Grayscale version of the first image.

grayscale_frame2.bmp: Grayscale version of the second image.

result.bmp: Image showing the motion detection results.

The terminal will display whether motion was detected:

Motion detected!

or

No motion detected.

Code Explanation

read_bmp: Reads a BMP file and returns the header, width, height, and pixel data.

write_bmp: Writes a BMP file with the given header and pixel data.

to_grayscale: Converts the image to grayscale.

detect_motion: Compares two grayscale images to detect motion.


