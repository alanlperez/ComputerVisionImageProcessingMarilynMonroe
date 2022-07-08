import cv2
import numpy

'''imread reads path of image so we can use image in code'''
image = cv2.imread("/Users/alanperez/PycharmProjects/pythonProject22/marilyn.bmp")

'''Here we have a list of gamma values'''
gammas = [0.04, 0.10, 0.20, 0.40, 0.67, 1, 1.5, 2.5, 5.0, 10.0, 25.0]

'''then we create a for loop so we go through each gamma one by one and apply it to the image 
   in order to use power transformation.'''
for gamma in gammas:
    '''We apply the gammas by creating an array to store our image using numpy.array. Inside 
       we are applying the equation of the Power Law (Gamma) Transformation.
       s = c*r^gamma. dtype = 'uint8' is just saying that it is an 8-bit unsigned integer.'''
    gamma_applied = numpy.array(255 * (image / 255) ** gamma, dtype = 'uint8')

    '''Here we are saving each power transformed image to a .jpg file in our for loop'''
    cv2.imwrite('gamma_transformation' + str(gamma) + '.jpg', gamma_applied)

