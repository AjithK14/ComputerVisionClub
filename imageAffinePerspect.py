import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('myCar.png')
rows,cols,ch = img.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,120],[200,80],[100,290]])
M = cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(img,M,(cols,rows))#(width,height)
plt.subplot(121)#1 row, 2 col figure; place it at leftmost column
plt.imshow(img)
plt.title('Before Transform')
plt.subplot(122)#1 row, 2 col figure; place it at right column
plt.imshow(dst) #puts image on figure
plt.title('After Transform')
plt.show() #displays actual figure
'''
img = cv2.imread('chess.png')
rows,cols,ch = img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]]) 
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300)) 
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
'''
