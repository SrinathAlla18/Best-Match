import cv2
import os
# Function matches the keypoints between the query image and the difference image
def perfect_match(query,matched_list):
    # convert both images into gray scale image
    img1 = cv2.cvtColor(diff2, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(query, cv2.COLOR_BGR2GRAY)
    # Create a sfit object
    sift = cv2.SIFT_create()
    # detecting the keypoints and descriptors
    keypoints_1, descriptors_1 = sift.detectAndCompute(img1, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(img2, None)
    # define a matcher object
    bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
    #  perform matches
    matches = bf.match(descriptors_1, descriptors_2)
    # length of matches gives us number of matches between both images
    matched_list.append(len(matches))
    return len(matches)
# This function implements a way to separate the region from aerial using the merged image.
def differnce_image(aerial,merged):
    diff1 = aerial.copy()
    # The absolute difference between aerial and merged is stored in diff1
    cv2.absdiff(merged, aerial, diff1)
    # The absolute difference between diff1 and merged is stored in diff2
    difference = aerial.copy()
    cv2.absdiff(diff1, merged, difference)
    return difference

if __name__ == "__main__":
    aerial = cv2.imread("aerial.png")
    merged = cv2.imread("merged.png")
    diff2=differnce_image(aerial,merged)
    dir = "query_images"
    matched=0
    name=''
    matched_list=[]
    for image in os.listdir(dir):
        image=dir+'/'+image
        query=cv2.imread(image)
        match_per_image=perfect_match(query,matched_list)
        if matched < match_per_image:
            matched = match_per_image
            name=image
    print("The name of the perfect match is {}" .format(name))
    print("Highest keypoint matches {} ".format(matched))
    print("The total list of matches".format(matched_list))



