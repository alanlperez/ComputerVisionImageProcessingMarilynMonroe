import cv2

'''imread reads path of image so we can use image in code'''
image = cv2.imread('/Users/alanperez/PycharmProjects/pythonProject24/marilyn.bmp', 0)

'''here we apply histogram equalization with the function cv2.equalizeHist and we save it into equalization'''
equalization = cv2.equalizeHist(image)

'''Then we save the result into a .jpg file'''
cv2.imwrite('histogram_equalization.jpg', equalization)
