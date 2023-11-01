import cv2
import numpy as np

path = "th.jpg"
kernel1 = np.ones((10, 10), np.uint8)
kernel2 = np.ones((5, 5), np.uint8)
kernel3 = np.ones((5, 5), np.float32) / 25
def findcolor(colorlow,colorup):

    img1 = cv2.filter2D(img, -1, kernel3)
    # cv2.imshow(tag+"1",img1)
    imgHSV = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)

    img2 = cv2.inRange(imgHSV,colorlow,colorup)
    img2 = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel1)
    img2 = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel2)
    contours ,h = cv2.findContours(img2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    return contours

def labelcolor(contours,color,tag):
    for cnt in contours:
        # epsilon = 0.05 * cv2.arcLength(cnt, True)
        # approx = cv2.approxPolyDP(cnt, epsilon, True)

        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.intp(box)

        (x, y, w, h) = cv2.boundingRect(box)
        cv2.putText(img, tag, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 1, cv2.LINE_AA)
        cv2.drawContours(img, [box], 0, color, 2)
        m = cv2.moments(cnt)
        cx = int(m['m10'] / m['m00'])
        cy = int(m['m01'] / m['m00'])
        cv2.circle(img, (cx, cy), 4, color, -1)


img = cv2.imread(path)
red = (0,0,255)
blue = (255,0,0)

# video = cv2.VideoCapture(0)
# while True:
#     ret ,img = video.read()
#     blue1_colorlow = np.array([100, 80, 70])
#     blue1_colorup = np.array([120, 255, 255])
#     blue1_contours = findcolor(blue1_colorlow, blue1_colorup)
#     # red2_colorlow = np.array([0, 170, 46])
#     # red2_colorup = np.array([7, 255, 255])
#     # red2_contours = findcolor(red2_colorlow, red2_colorup)
#     red1_colorlow = np.array([156, 43, 46])
#     red1_colorup = np.array([179, 255, 255])
#     red1_contours = findcolor(red1_colorlow, red1_colorup)
#
#     labelcolor(red1_contours,blue,"red")
#     # labelcolor(red2_contours,blue,"red")
#     labelcolor(blue1_contours,red,"blue")
#
#     cv2.imshow("1", img)
#
#     if cv2.waitKey(1) == ord('q'):
#         break
# video.release()

blue1_colorlow = np.array([100, 80, 70])
blue1_colorup = np.array([120, 255, 255])
blue1_contours = findcolor(blue1_colorlow, blue1_colorup)
red2_colorlow = np.array([0, 170, 46])
red2_colorup = np.array([7, 255, 255])
red2_contours = findcolor(red2_colorlow, red2_colorup)
red1_colorlow = np.array([156, 43, 46])
red1_colorup = np.array([179, 255, 255])
red1_contours = findcolor(red1_colorlow, red1_colorup)

labelcolor(red1_contours,blue,"red")
labelcolor(red2_contours,blue,"red")
labelcolor(blue1_contours,red,"blue")

cv2.imshow("1", img)

cv2.waitKey(0)