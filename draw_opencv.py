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

# '''
# 查看opencv 中所有的EVENT 事件
# '''
# import cv2 as cv
# event = [i for i in dir(cv) if 'EVENT' in i ]
# print("opencv 中EVENT：",event)


'''根据我
们选择的模式在拖动鼠标时绘制矩形或者是圆圈（就像画图程序中一样）。所以
我们的回调函数包含两部分，一部分画矩形，一部分画圆圈。这是一个典型的
例子他可以帮助我们更好理解与构建人机交互式程序，比如物体跟踪，图像分
割等。
'''

import cv2 as cv
import numpy as np

# 当鼠标按下时候为True
drawing = False
# 如果mode 为true 绘制矩形。按下'm' 变成绘制曲线。

mode = True
ix,iy = -1,-1

# 创建回调函数
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
#     当按下左键是返回起始位置坐标
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
#       当鼠标左键按下并移动是绘图图形。event 可以查看移动，flag 查看是否按下
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
        if drawing == True:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
#                  绘制圆圈，小圆点连在一起就成了线，
                cv.circle(img,(x,y),radius=50,color=(0,0,255))
#               下面注释掉的代码是起始点为圆心，起点到终点为半径的
#                r=int(np.sqrt((x-ix)**2+(y-iy)**2))
#                cv2.circle(img,(x,y),r,(0,0,255),-1)
# 当鼠标松开停止绘画。
    elif event==cv.EVENT_LBUTTONUP:
        drawing==False
#       if mode==True:
#           cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
#       else:
#           cv2.circle(img,(x,y),5,(0,0,255),-1)
img = np.zeros((1024,1024,3),np.uint8)
cv.namedWindow("image",cv.WINDOW_NORMAL)
cv.setMouseCallback("image",draw_circle)

while(True):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xff
    if k==ord('m'):
        mode = not mode
    elif k==ord('q'):
        break