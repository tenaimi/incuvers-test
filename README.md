# Coding challenge

## Instructions

Clone the `test` repo incuvers/test, and add it to you GitHub profile. Do not fork it, just copy it as your own.
 
Answer the question and submit your answers as feature branches, name the branches `feature-Q1` and `feature-Q2`.

Send us a link to your Github page where you copied the questions and the answers are found as  branches. Commits time-stamped any time later than one hour after the link has been shared with you will not be considered.

As preparation, you may want to have a working installation of Python3 with the following python modules: Numpy, Scipy, OpenCV, Matplotlib. 


### Background

The exposure time is a critical photographic parameter. It determines for how long camera pixels are sensitive to light. Your task will be to solve common exposure time problems using python. You can (and are encouraged to) use numerical libraries like numpy. Some of the tasks can probably be solved using one-liners from imaging libraries (like OpenCV, PILLOW). You obviously cannot use those solutions. You are allowed to use these imaging libraries only to open, save, and convert image files.

### A single grayscale pixel
During the exposure time, photons hit a sensor and creates an electrical current that charges a capacitor. This process is allowed to continue for some time called the exposure time. After the exposure time runs out, a voltage reading is taken on the capacitor and this value (after being processed) is interpreted as a grayscale pixel value between 0 and 255. The longer the sensor is exposed to light, the more current can charge the capacitor and the higher the pixel value.

### A grayscale image
An image is constructed by recreating the preceding situation over a two-dimensional grid of sensors. The resulting image is a 2D array of pixels values between 0-255. The pixels are arranged as a two-dimensional array, of dimensions w x h that corresponds to the physical arrangement of the photo-sensitive grid.

### A color RGB image
We will provide a set of images saved as PNG files. These images have three color channels for red green and blue instead of the single grayscale channel described above. You can average these channels to create the greyscale channel, or simply choose any one of the color channels to play the role as the grayscale channel. 


## Task 1

A student forgot to properly setup the incubator’s camera and acquired hundreds of images that look too dim. Next time, the student will have to increase the exposure time, but now it's too late. Your task is to write a python script to “fix” the image called `exposure-4100.png` under the `images` directory.

Explain a few ways that you think could “fix” the images. Test your ideas by implementing them and viewing the results. This can be quick and dirty code. Log your exploration process and resulting images). Some ideas will be better than the others, it is important to explore by trial and error.



## Task 2

Manually adjusting the exposure time can be tricky. Unfortunately, the image quality can suffer greatly if it is not chosen properly. You are to write a function that guesses the ideal exposure time for a particular lighting setup.

You will be given a list of images under the `images` directory obtained at different exposure times to simulate the image acquisition.  The images are named in the format `exposure-<TIME>.png`, where `<TIME>` is the exposure time in microseconds used to capture the image.

By eye, you should be able to find the best of those images, but we can do better yet! Can you guess what the exposure time should be in order to acquire the best image?

