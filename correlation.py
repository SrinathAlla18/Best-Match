import imreg_dft as ird
import cv2
import numpy as np
import os

def differnce_image(aerial,merged):
    diff1 = aerial.copy()
    # The absolute difference between aerial and merged is stored in diff1
    cv2.absdiff(merged, aerial, diff1)
    # The absolute difference between diff and merged is stored in diff2
    diff2 = aerial.copy()
    cv2.absdiff(diff1, merged, diff2)
    return diff2

def tranformed_image(diff2,query):
    # Both the images are converted into grayscale
    img1 = cv2.cvtColor(diff2, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(query, cv2.COLOR_BGR2GRAY)
    # The imreg_dft module helps us
    # result is a dictionary that stores the scale,rotation, translation, and transformed query image
    result = ird.similarity(img1, img2)
    # timg is  the transformed  query image.
    timg = np.array(result['timg'])
    return timg

def correlation_coefficent(aerial,timg):
    # co-relation between the transformed image and the sample image
    aerial = cv2.cvtColor(aerial, cv2.COLOR_BGR2GRAY)
    #  both the images are flattened to perform the correlation operation on the images
    c= np.corrcoef(aerial.flat, timg.flat)
    # coeff is the correlation coefficient between both the images.
    coeff = c[0, 1]
    return coeff

if __name__ == "__main__":
    aerial = cv2.imread("aerial.png")
    merged = cv2.imread("merged.png")
    diff2=differnce_image(aerial,merged)
    dir = "query_images"
    largest_coeff = 0
    address =''
    for image in os.listdir(dir):
        image=dir+'/'+image
        query=cv2.imread(image)
        timg = tranformed_image(diff2, query)
        coeff= correlation_coefficent(aerial, timg)
        if largest_coeff<coeff :
            largest_coeff=coeff
            address=image
    print("The largest coefficient is {}".format(largest_coeff))
    print("The name of the perfect match is {}" .format(address))


