#MOSTRA TAMANHO DA IMAGEM
import cv2 as cv

def size(img):
    try:
        if img is None:
            print("Error 404")
        else:
            read_img = cv.imread(img)
            img_height_lenght = read_img.shape[:2]
            return img_height_lenght
    except cv.Error as e:  

        print(e)
