import cv2
import numpy as np

# 크기 변환
src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

dst = cv2.resize(src, dsize=(320, 240))
dst2 = cv2.resize(src, dsize=(0,0), fx=1.5, fy=1.2)

cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)

# 회전
src2 = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

dst3 = cv2.rotate(src2, cv2.ROTATE_90_CLOCKWISE)
dst4 = cv2.rotate(src2, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow('dst3', dst3)
cv2.imshow('dst4', dst4)

cv2.waitKey()
cv2.destroyAllWindows()