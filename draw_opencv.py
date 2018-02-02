# import numpy as np
# import cv2 as cv
#
# # create a black image
# cv.namedWindow("image",cv.WINDOW_NORMAL)
# img = np.zeros((1024,1024,3),np.uint8)
# print(img.shape)
# #draw a diagonal blue line with thickness (线条的粗细) of 5px
# cv.line(img,(0,0),(1024,1024),(255,0,0),thickness=5)
#
# # draw a rectangle
# cv.rectangle(img,(512-200,512-200),(512+200,512+200),(0,255,0),thickness=10)
#
# # draw a circle
# cv.circle(img,(512,512),radius=200,color=(0,0,255),thickness=20)
#
# # draw a ellipse
# cv.ellipse(img,(512,512),(200,400),angle=90,startAngle=0,endAngle=180,color=(255,255,0),thickness=30)
#
# # draw a poly lines
# pts = np.array([[128,128],[128,128+200],[128+400,128+400],[128+200,128],[234,456]],np.int32)
# pts = pts.reshape((-1,1,2))
# cv.polylines(img,[pts],isClosed=True,color=(0,255,255),thickness=20)
#
# # add text
# font = cv.FONT_HERSHEY_SIMPLEX
# cv.putText(img,"alexChen",org=(196,512),fontFace=font,fontScale=5,color=(255,255,0),thickness=10)
#
# cv.imshow("image",img)
# cv.waitKey(0)
# cv.destroyAllWindows()


# import cv2 as cv
# import numpy as np
#
# '''
# 把鼠标当画笔,cv2.setMouseCallback()
# 首先我们来创建一个鼠标事件回调函数，但鼠标事件发生是他就会被执行。
# 鼠标事件可以是鼠标上的任何动作，比如左键按下，左键松开，左键双击等。
# 我们可以通过鼠标事件获得与鼠标对应的图片上的坐标。根据这些信息我们可
# 以做任何我们想做的事。你可以通过执行下列代码查看所有被支持的鼠标事件。
# '''
#
# def draw_circle(event,x,y,flags,param):
#     if event == cv.EVENT_LBUTTONDBLCLK:
#         cv.circle(img, (x, y), 100, (255, 0, 0), -1)
#
# img = np.zeros((1024,1024,3),np.uint8)
# cv.namedWindow("image",cv.WINDOW_NORMAL)
# cv.setMouseCallback("image",draw_circle)
#
# while(True):
#     cv.imshow("image",img)
#     if cv.waitKey(20) & 0xff==ord("q"):
#         break
# cv.destroyAllWindows()

