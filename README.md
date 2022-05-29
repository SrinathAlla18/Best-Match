# Best-Match
RESULTS:

SIFT method results:
The name of the perfect match is
Highest keypoint matches
The total list of matches


correlation method results:
The largest coefficient is 0.1435698
The name of the perfect match is 



The main aim is to find the best match between the query images and the aerial image.
 I used two methods to solve the problem
1) correlation method:
 I have used the Imreg library, which implements an FFT-based technique for translation, rotation, and scale-invariant image registration. In the first step, I used the merged and the aerial image to extract the patch(Difference image)  that needed to compare with the query images. In the second step, I used the Imreg library to transform the query images by understanding the transformation between the query image and the difference image. In the final step, I did a cross-correlation between the aerial image and the transformed query image to produce the correlation coefficient. The query image that gives the highest coefficient value is the image that matches best with the aerial image.

Documentation for Imreg:
https://imreg-dft.readthedocs.io/en/latest/api.html

2) SIFT Method:
In the first step, I used the merged and the aerial image to extract the patch(Difference image)  that needed to compare with the query images.
In the second step, using the SFIT algorithm, we will generate the key points and descriptors for both the difference image and query image. The descriptors generated for both images will be matched with each other using BFMatcher, which helps to find the best matcher among the descriptors of both images. The query image which will have more matches with the difference image of the aerial and merged image will be the best-fit image.

