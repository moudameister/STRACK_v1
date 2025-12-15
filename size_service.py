#MOSTRA TAMANHO DA IMAGEM
import cv2 as cv
import numpy as np

def size(img):
    try:
        if img is None:
            print("Error 404")
        else:
            decoded_img = cv.imdecode(np.frombuffer(img, np.uint8), cv.IMREAD_COLOR)
            img_height_lenght = decoded_img.shape[:2]
            return img_height_lenght
    except cv.Error as e:  
        print(e)