import cv2
import numpy as np
import sys



img= cv2.imread('testpic.jpg',1) #1 puts it in color
#print('Original Dimensions : ',img)

data = np.random.random((10,10))

# fig, ax = plt.subplots()
# ax.imshow(data, interpolation='none')
#
# mpldatacursor.datacursor(hover=True, bbox=dict(alpha=1, fc='w'))
# #plt.show()

width = int(img.shape[1] * 50 / 100)
height = int(img.shape[0] * 50/100)
width=500
height=500
dim = (width,height)
resized = cv2.resize(img,dim)

#
# center= (500,200)
# #size=(300,200)
# axes=(250, 100)
# #radius= 300
# color= (255, 255, 255) #255 is red RGB
# angle= -40
# start_angle = 0
# end_angle = 360
#
# cv2.ellipse(resized, center, axes, angle, start_angle, end_angle, color, thickness=3, lineType=8, shift=0 )
# #cv2.circle(img, center, radius, color, thickness=1, lineType=8, shift=0)
#
# center= (400,500)
# #size=(300,200)
# axes=(200, 50)
# #radius= 300
# color= (255, 255, 255) #255 is red
# angle=10
# start_angle = 0
# end_angle = 360
#
# cv2.ellipse(resized, center, axes, angle, start_angle, end_angle, color, thickness=3, lineType=8, shift=0 )




cv2.imshow('testpicresize', resized)
cv2.imwrite('testpicresize.jpg', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
