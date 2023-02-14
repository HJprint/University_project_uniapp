import numpy as np
import cv2
filename = 'elon.jpeg'

def resizeImage(image):
    scale_ratio = 0.3
    width = int(image.shape[1] * scale_ratio)
    height = int(image.shape[0] * scale_ratio)
    new_dimensions = (width, height)
    resized = cv2.resize(image, new_dimensions, interpolation = cv2.INTER_AREA)

    return resized

def findCountours(image):

    contoured_image = image
    gray = cv2.cvtColor(contoured_image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 30, 100)
    contours, hierarchy = cv2.findContours(edged,
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(contoured_image, contours, contourIdx=-1, color=1, thickness=1)
    cv2.imshow('Image after countouring', contoured_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return contoured_image

def ColorQuantization(image, K=4):
    Z = image.reshape((-1, 3))
    Z = np.float32(Z)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10000, 0.0001)
    compactness, label, center = cv2.kmeans(Z, K, None, criteria, 1, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    es2 = res.reshape((image.shape))

    return res2

if __name__ == "__main__":

    image = cv2.imread(filename)
    resized_image = resizeImage(image)
    coloured = ColorQuantization(resized_image)
    contoured = findCountours(coloured)
    final_image = contoured
    save_q = input("Save the image? [y]/[n] ")

    if save_q == "y":

        cv2.imwrite("cartoonized_"+ filename, final_image)
        print("Image saved!")
