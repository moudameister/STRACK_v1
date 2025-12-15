#CONVERTE PARA HSV, DESTACA E DIZ PORCENTAGEM
import cv2 as cv
import numpy as np

def hsv_mask(img):
    bin_mask = np.array([])
    if img is None:
        print("Imagem vazia.")
    else:
        try:
            bgr_img = cv.imread(img)
            hsv_img = cv.cvtColor(bgr_img, cv.COLOR_BGR2HSV)
            green_min = np.array([25, 100, 100])
            green_max = np.array([80, 255, 255])
            bin_mask = cv.inRange(hsv_img, green_min, green_max)
            white_pixels = np.count_nonzero(bin_mask)
            green_percent = np.round((white_pixels / bin_mask.size) * 100)
            print(green_percent)
            return bin_mask, green_percent
        except cv.Error as e:
            print(e)