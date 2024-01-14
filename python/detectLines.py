import cv2 

import numpy as np 

image = cv2.imread('hi.jpeg') 


min_val = 170
lower_red = np.array([min_val, min_val, min_val], dtype = "uint8") 


max_val = 190
upper_red= np.array([max_val, max_val, max_val], dtype = "uint8")

mask = cv2.inRange(image, lower_red, upper_red)

detected_output = cv2.bitwise_and(image, image, mask =  mask) 

cv2.imwrite("detectLines.png", detected_output) 


cv2.imshow("red color detection", detected_output) 

cv2.waitKey(0) 



# ### 
# import cv2
# import numpy as np
# import matplotlib
# from matplotlib.pyplot import imshow
# from matplotlib import pyplot as plt

# # white color mask
# img = cv2.imread(filein)
# #converted = convert_hls(img)
# image = cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
# lower = np.uint8([0, 200, 0])
# upper = np.uint8([255, 255, 255])
# white_mask = cv2.inRange(image, lower, upper)
# # yellow color mask
# lower = np.uint8([10, 0,   100])
# upper = np.uint8([40, 255, 255])
# yellow_mask = cv2.inRange(image, lower, upper)
# # combine the mask
# mask = cv2.bitwise_or(white_mask, yellow_mask)
# result = img.copy()
# cv2.imshow("mask",mask) 