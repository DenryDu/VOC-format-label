# from PIL import Image # ddy_2020_2_1_20:07        change Image to cv2
import cv2
import os


# ddy_2020_2_1_19:45        //to go through on folder and crop all image(ends with .jpeg) to a square, then resize to 300x300 to fit VOC format

# specify the directory path
directory = "JPEGImages"

# go through the dir to find all the image file
for filename in os.listdir(directory):
    if filename.endswith(".jpeg"):
        imagefile = os.path.join( directory, filename)
        im = cv2.imread(imagefile)
        #cv2.imshow("origin", im)
        #y = im.shape[0]
        #x = im.shape[1]
        #size = x if x < y else y
        #y_begin = 0 if y == size else int((y-size)/2)
        #x_begin = 0 if x == size else int((x-size)/2)
        #im_crop = im[y_begin: y_begin+size, x_begin: x_begin+size]
        #cv2.imshow("cropped", im_crop)
        #cv2.waitKey(1000)
 
        # resize image
        #im_resize = cv2.resize(im_crop, (300, 300), interpolation = cv2.INTER_AREA)         
        #im_resize = cv2.resize(im, (300, 300), interpolation = cv2.INTER_AREA)         
        im_resize =  cv2.resize(im, (300, 300)).astype(np.float32)
        cv2.imshow("resized", im_resize)
        cv2.waitKey(1000)

        #cv2.imwrite(imagefile, im_resize) 
cv2.destroyAllWindows()
