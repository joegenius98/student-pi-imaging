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
from matplotlib import pyplot as plt
import numpy as np



import glob

image_folder = pathlib.Path('.')
print(image_folder.iterdir())
imgs = [x for x in image_folder.iterdir() if ((x.suffix.lower() == '.jpg') or (x.suffix.lower() == '.png'))]
imgs.sort()
print(imgs)
image=imgs[16]


print(type(image))


image = cv2.imread(str(image))

b = image.copy()
# set green and red channels to 0
b[:, :, 1] = 0
b[:, :, 2] = 0

perfect = image.copy()
perfect[:,:,1] += 10
perfect[:,:,1] *= 2

average = (perfect[:,:,0] + perfect[:,:,1] + perfect[:,:,2]) / 3
average += 30
average *= 2

# im_color = cv2.applyColorMap(average, cv2.COLORMAP_HOT)


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

# cv2.imshow('image', perfect)
# cv2.waitKey(0)
# # RGB - Blue
# cv2.imshow('image21', perfect[:,:,0])
# cv2.waitKey(0)
#
# # RGB - Green
# cv2.imshow('image22', perfect[:,:,1])
# cv2.waitKey(0)
#
# # RGB - Red
# cv2.imshow('image23', perfect[:,:,2])
# cv2.waitKey(0)
# cv2.imshow('Hayden Ferguson', image)
# cv2.waitKey(0)
# cv2.imshow('image24', average)
# cv2.waitKey(0)

# images = [cv2.imread(file) for file in glob.glob("*.jpg")]
# print(images[0])


fig = plt.figure(figsize=[10, 10])
ax = fig.add_subplot(111)
ax.set_axis_off()
plt.colorbar(ax.imshow(average, cmap = 'hot'))
plt.show()



#

#cv2.waitKey(0)





