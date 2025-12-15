import cv2 as cv

def resize(img, a, b):
    try:
        if img is None:
            print("not found")
        else:
            img_read = cv.imread(img)
            new_height, new_lenght = a, b
            new_size = cv.resize(img_read(new_lenght,new_height), interpolation = cv.INTER_AREA)
            return new_size
    except cv.Error as e:

        print(e)
