from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS # dictionaries for exiftags and gpstags names
import cv2 as cv # opencv package
import piexif
import piexif.helper

import pathlib # standard library package for working with file paths
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

import cv2
import numpy as np

image_folder = pathlib.Path('.')
imgs = [x for x in image_folder.iterdir() if ((x.suffix.lower() == '.jpg') or (x.suffix.lower() == '.png'))]

image=imgs[2]
print(type(image))


image = cv2.imread(str(image))

b = image.copy()
# set green and red channels to 0
b[:, :, 1] = 0
b[:, :, 2] = 0

perfect = image.copy()
perfect[:,:,1] -= 1
perfect[:,:,1] *= 2

average = perfect[:,:,0]+perfect[:,:,1]+perfect[:,:,2]
average = average/3
average += 10
average *= 2


#im = cv2.imread(average, 0)
#average = cv2.equalizeHist(im)

g = image.copy()


# set blue and red channels to 0
#g+=100


g[:, :, 0] = 0
g[:, :, 2] = 0

r = image.copy()
# set blue and green channels to 0
r[:, :, 0] = 0
r[:, :, 1] = 0

cv2.imshow('', perfect)
# RGB - Blue
cv2.imshow('', perfect[:,:,0])

# RGB - Green
cv2.imshow('', perfect[:,:,1])

# RGB - Red
cv2.imshow('', perfect[:,:,2])

cv2.imshow('', average)

#cv2.waitKey(0)





