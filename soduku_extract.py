from imutils.perspective import four_point_transform
from skimage.segmentation import clear_border
import numpy as np
import imutils
import cv2
import os
img  = cv2.imread("soduku.png")

##find the empty cell in sodoku board from img inputed and simulated into x in notepad file ( idea: count while/Black pixel)


def find_empty_cell(image, debug=False):
    #chuyển đổi và xử lý tiền ảnh
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 10)
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 3)
    thresh = cv2.bitwise_not(thresh)

    #khởi tạo các thông số ảnh để tìm viền bảng
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

    #tìm được 4 đỉnh của bảng dựa vào tính liên tục pixel và cắt ngang dọc
    for i in cnts:
        # approximate the contour
        per = cv2.arcLength(i, True)
        approx = cv2.approxPolyDP(i, 0.02 * per, True)
        if len(approx) == 4:
            break

    #nhận ảnh đã cắt và tiền xử lý các ô k giá trị -> đen, có giá trị -> trắng
    image = four_point_transform(thresh, approx.reshape(4, 2))
    kernel = np.ones((5, 5), np.uint8)
    image = cv2.dilate(image, kernel, iterations=6)
    image = cv2.erode(image, kernel, iterations=6)

    #dài rộng ảnh hiện tại
    (h,w) = image.shape

    # Tạo file mới
    f = open('output.txt', 'x')
    #Quét từng ô ảnh trong bảng để tính tổng số pixel trắng/đen để xác định ô có chứa giá trị hay k
    for i in range(0,9):
        for j in range(0,9):
            x = round(w / 9 + 1) * j
            y = round(h / 9 + 1) * i
            crop = image[y:y + round(h / 9), x:x + round(w / 9)]
            white_pix = np.sum(crop == 255)
            black_pix = np.sum(crop == 0)
            if black_pix > 600:
                if j != 8:
                    f.write(' ')
                if j == 8:
                    f.write(" \n")
            if white_pix > 600:
                if j != 8:
                    f.write('X')
                if j == 8:
                    f.writelines("X\n")
    #Đóng file
    f.close()

    #Hiển thị ảnh minh họa
    if debug:
        cv2.imshow("Puzz", image)
        cv2.waitKey(0)

find_empty_cell(img, debug=True)