import numpy as np
import cv2

img = cv2.imread('images/exposure-4100.png',0)

img.resize((img.shape[0], img.shape[1], 1))
new_image = np.repeat(img.astype(np.uint8), 3, 2)


imS = cv2.resize(new_image, (960, 540)) 

cv2.imshow('image', imS)
cv2.waitKey(0)
cv2.destroyAllWindows()