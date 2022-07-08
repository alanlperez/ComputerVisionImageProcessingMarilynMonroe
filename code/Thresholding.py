import cv2

'''imread reads path of image so we can use image in code'''
image = cv2.imread('/Users/alanperez/PycharmProjects/pythonProject23/marilyn.bmp', 1)

'''thresholdValue is our threshold value, threshold1 will hold our binary image. cv2.threshold is a function that allows sets a threshold and 
   allows us to convert an image to a binary image. image is the image that we read in the previous line. 
   127 is the threshold value we set. 255 is the maximum value that pixel intensity bigger than 127 are converted to 255.
   Then we set the threshold type to 'THRESH_BINARY' '''
thresholdValue, threshold = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

cv2.imwrite('thresholding.jpg', threshold)
