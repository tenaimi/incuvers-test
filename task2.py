import cv2 as cv
import numpy as np

def main():
    images = ['exposure-100.png', 'exposure-4100.png', 'exposure-8100.png', 'exposure-12100.png', 'exposure-16100.png', 'exposure-20100.png']
    guess_lightning(images)

def guess_lightning(images): 
    for i in range(len(images)):
        path = './images/' + images[i]
        image = cv.imread(path)
        if image is None:
            print('Could not open or find the image: ', path)
            exit(0)
        exposure_time = images[i][9:][:-4]
        new_image = np.zeros(image.shape, image.dtype)

        alpha = 1.0 # Simple contrast control
        beta = 0    # Simple brightness control

        print(image.shape[0], image.shape[1], image.shape[2])
        for y in range(image.shape[0]):
            for x in range(image.shape[1]):
                for c in range(image.shape[2]):
                    new_image[y,x,c] = np.clip(alpha*image[y,x,c] + beta, 0, 255)

        cv.imshow('Original Image', image)
        cv.imshow('New Image', new_image)

        # Wait until user press some key
        cv.waitKey(0)



main()