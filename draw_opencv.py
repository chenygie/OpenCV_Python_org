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

# import cv2 as cv
# import numpy as np
#
# # 当鼠标按下时候为True
# drawing = False
# # 如果mode 为true 绘制矩形。按下'm' 变成绘制曲线。
#
# mode = True
# ix,iy = -1,-1
#
# # 创建回调函数
# def draw_circle(event,x,y,flags,param):
#     global ix,iy,drawing,mode
# #     当按下左键是返回起始位置坐标
#     if event == cv.EVENT_LBUTTONDOWN:
#         drawing = True
#         ix,iy = x,y
# #       当鼠标左键按下并移动是绘图图形。event 可以查看移动，flag 查看是否按下
#     elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
#         if drawing == True:
#             if mode == True:
#                 cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
#             else:
# #                  绘制圆圈，小圆点连在一起就成了线，
#                 cv.circle(img,(x,y),radius=50,color=(0,0,255))
# #               下面注释掉的代码是起始点为圆心，起点到终点为半径的
# #                r=int(np.sqrt((x-ix)**2+(y-iy)**2))
# #                cv2.circle(img,(x,y),r,(0,0,255),-1)
# # 当鼠标松开停止绘画。
#     elif event==cv.EVENT_LBUTTONUP:
#         drawing==False
# #       if mode==True:
# #           cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
# #       else:
# #           cv2.circle(img,(x,y),5,(0,0,255),-1)
# img = np.zeros((1024,1024,3),np.uint8)
# cv.namedWindow("image",cv.WINDOW_NORMAL)
# cv.setMouseCallback("image",draw_circle)
#
# while(True):
#     cv.imshow('image',img)
#     k = cv.waitKey(1) & 0xff
#     if k==ord('m'):
#         mode = not mode
#     elif k==ord('q'):
#         break
# cv.destroyAllWindows()

import  cv2 as cv
import numpy as np

'''
制造椒盐噪音
'''

# img = cv.imread("skin.jpg")
# cv.namedWindow("image",cv.WINDOW_NORMAL)
# cv.namedWindow("image2",cv.WINDOW_NORMAL)
# rows,cols,dims = img.shape
# for i in range(5000):
#     x = np.random.randint(0,rows)
#     y = np.random.randint(0,cols)
#     img[x,y,:] = 255
# cv.imshow("image",img)
# cv.imwrite("zaoying.jpg",img)
# median = cv.medianBlur(img,5)
# cv.imshow("image2",median)
# cv.waitKey(0) & 0xff ==ord("q")


# import cv2 as cv
# import numpy as np
# '''
# 函数：cv2.getTrackbarPos()， cv2.creatTrackbar()等。
# 创建一个简单的程序：通过调节滑动条来设定画板颜色。我们
# 要创建一个窗口来显示显色，还有三个滑动条来设置 B， G， R 的颜色。当我们
# 滑动滚动条是窗口的颜色也会发生相应改变。默认情况下窗口的起始颜色为黑。
# cv2.getTrackbarPos() 函数的一个参数是滑动条的名字，第二个参数
# 是滑动条被放置窗口的名字，第三个参数是滑动条的默认位置。第四个参数是
# 滑动条的最大值，第五个函数是回调函数，每次滑动条的滑动都会调用回调函
# 数。回调函数通常都会含有一个默认参数，就是滑动条的位置。在本例中这个
# 函数不用做任何事情，我们只需要 pass 就可以了。
# 滑动条的另外一个重要应用就是用作转换按钮。默认情况下 OpenCV 本
# 身不带有按钮函数。所以我们使用滑动条来代替。在我们的程序中，我们要创
# 建一个转换按钮，只有当装换按钮指向 ON 时，滑动条的滑动才有用，否则窗
# 户口都是黑的。
# '''
#
# def nothing(x):
#     pass
#
# # 创建一副黑色图像
# img = np.zeros((300,512,3),np.uint8)
# cv.namedWindow("image",cv.WINDOW_NORMAL)
#
# cv.createTrackbar('R','image',0,255,nothing)
# cv.createTrackbar('G','image',0,255,nothing)
# cv.createTrackbar('B','image',0,255,nothing)
#
# switch = '0:OFF \n 1:ON'
# cv.createTrackbar(switch,"image",0,1,nothing)
#
# while(True):
#     cv.imshow("image",img)
#     k = cv.waitKey(1) & 0xFF
#     if k==27:
#         break
#     r = cv.getTrackbarPos(trackbarname="R",winname="image")
#     g = cv.getTrackbarPos(trackbarname="G",winname="image")
#     b = cv.getTrackbarPos(trackbarname="B",winname="image")
#     s = cv.getTrackbarPos(trackbarname=switch,winname="image")
#     if s==0:
#         img[:] = 0
#     else:
#         img[:] = [b,g,r]
# cv.destroyAllWindows()

# import cv2
# import numpy as np
# def nothing(x):
#     pass
# # 创建一副黑色图像
# img=np.zeros((300,512,3),np.uint8)
# cv2.namedWindow('image')
# cv2.createTrackbar('R','image',0,255,nothing)
# cv2.createTrackbar('G','image',0,255,nothing)
# cv2.createTrackbar('B','image',0,255,nothing)
# switch='0:OFF\n1:ON'
# cv2.createTrackbar(switch,'image',0,1,nothing)
# while(1):
#     cv2.imshow('image',img)
#     k=cv2.waitKey(1)&0xFF
#     if k==27:
#         break
#     r=cv2.getTrackbarPos('R','image')
#     g=cv2.getTrackbarPos('G','image')
#     b=cv2.getTrackbarPos('B','image')
#     s=cv2.getTrackbarPos(switch,'image')
#     if s==0:
#      img[:]=0
#     else:
#       img[:]=[b,g,r]
# cv2.destroyAllWindows()


import numpy as np
import cv2 as cv

''''
创建一个画板，可以自选各种颜色的画笔绘画各种图
形。
'''
def nothing(x):
    pass

# 当鼠标按下时变成为True绘制距形，按下'm'变成绘制曲线
mode = True
ix,iy = -1,-1

# create recall function
def draw_circle(event,x,y,flags,param):
    r = cv.getTrackbarPos("R","image")
    g = cv.getTrackbarPos("G","image")
    b = cv.getTrackbarPos("B","image")
    color = (b,g,r)
    global ix,iy,drawing,mode
    # 当按下左键是返回起始位置
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
        # 当鼠标左键按下并移动时绘制圆形，event可以看移动，flags查看是否按下。
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
        if drawing==True:
            if mode==True:
                cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                # 绘制圆圈
                cv.circle(img,(x,y),300,(255,255,255),-1)
    elif event==cv.EVENT_LBUTTONUP:
        drawing = False
img = np.zeros((1024,1024,3),np.uint8)
cv.namedWindow("image",cv.WINDOW_NORMAL)
cv.createTrackbar("R","image",  0,255,nothing)
cv.createTrackbar("G","image",0,255,nothing)
cv.createTrackbar("B","image",0,255,nothing)
cv.setMouseCallback("image",draw_circle)
while(True):
    cv.imshow("image",img)
    r = cv.getTrackbarPos("R","image")
    g = cv.getTrackbarPos("G","image")
    b = cv.getTrackbarPos("B","image")
    img[:] = [b,g,r]
    k = cv.waitKey(1) & 0xff
    if k==ord("m"):
        mode = not mode
    elif k==27:
        break
cv.destroyAllWindows()