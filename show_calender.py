import cv2

img = "calender.png"
img = cv2.imread(img)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
