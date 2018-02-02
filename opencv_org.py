# import numpy as np
# import cv2 as cv

# img = cv.imread("skin.jpg",0)
# cv.imshow("image",img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# cv.namedWindow("image",cv.WINDOW_NORMAL)
# cv.imshow("image",img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# import  numpy as np
# import cv2 as cv
#
# img = cv.imread("skin.jpg",0)
# cv.namedWindow("image",cv.WINDOW_NORMAL)
# cv.imshow("image",img)
# k = cv.waitKey(0) & 0xff
# if k == 27: #  means ESC key to exit
#     cv.destroyAllWindows()
# elif k == ord('s'):
#     cv.imwrite("skingray.png",img)
#     cv.destroyAllWindows()

# import numpy as np
# import cv2 as cv
# from matplotlib import pyplot as plt
#
# img = cv.imread("skin.jpg",0)
# plt.imshow(img,cmap='gray',interpolation='bicubic')
# plt.xticks([])
# plt.yticks([])
# plt.show()

# import numpy as np
# import cv2 as cv
#
# cap  = cv.VideoCapture(0)
#
# while(True):
#     ret,frame = cap.read()
#
#     gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
#
#     cv.imshow("frame",gray)
#     if cv.waitKey(1) & 0xff ==ord("q"):
#         break
# cap.release()
# cv.destroyAllWindows()
#
# import numpy as np
# import cv2 as cv
#
# cap = cv.VideoCapture(0)
# fourcc = cv.VideoWriter_fourcc(*"XVID")
# size = (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
# fps = 20.0
# out = cv.VideoWriter("output1.mov",fourcc,fps,size)
# cv.namedWindow("frame",cv.WINDOW_NORMAL)
# while(cap.isOpened()):
#     ret,frame = cap.read()
#     if ret == True:
#         # 对获取的视频进行反转
#         # flip(src_img, des_img, 1); // 1
#         # 代表水平方向旋转180度
#         # // flip(src_img, des_img, 0); // 0
#         # 代表垂直方向旋转180度
#         # // flip(src_img, des_img, -1); // -1
#         # 代表垂直和水平方向同时旋转
#         frame = cv.flip(frame,180)
#         cv.imshow("frame",frame)
#         out.write(frame)
#         if cv.waitKey(1) & 0xff == ord('q'):
#             break
# cap.release()
# out.release()
# cv.destroyAllWindows()


