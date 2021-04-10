import numpy as np
import matplotlib.pylab as plt
import matplotlib.image as img
import scipy.misc
import sys
import cv2
from scipy import misc
imSrc = plt.imread(r'C:\Users\herman\Desktop\滤波\girl.jpg')

# plt.imshow(imSrc)
# plt.show()
print(imSrc.shape)
hei = imSrc.shape[0]
wid = imSrc.shape[1]
channel = imSrc.shape[2]
#print(imSrc)

im_new_sourcesize = np.copy(imSrc)
im_new_smallsize = np.zeros((int(hei/2), int(wid/2),channel),dtype=np.uint8)

for c in range(0,channel):
        for row in range(0,hei-1,2):
                for col in range(0,wid-1,2):
                    # output small size picture
                    avg = np.mean(imSrc[row:row+1,col:col+1,c])
                    im_new_smallsize[int(row/2), int(col/2), c] = avg
                    #print(im_new_smallsize[int(row/2), int(col/2), c])

                    # output source size picture
                    avg = np.mean(imSrc[row:row+1,col:col+1,c])
                    im_new_sourcesize[row,col,c] = avg
                    im_new_sourcesize[row+1, col, c] = avg
                    im_new_sourcesize[row, col+1, c] = avg
                    im_new_sourcesize[row+1, col+1, c] = avg
#print(imdest)
#print(im_new)
img.imsave('new_SourceSize.jpg',im_new_sourcesize)
img.imsave('new_SmallSize.jpg',im_new_smallsize)
#cv2.imwrite('new_girl.jpg', imdest)



