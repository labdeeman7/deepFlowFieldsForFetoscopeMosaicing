import cv2
import numpy as np
import matplotlib.pyplot as plt
import flowiz as f

# test for farneback's method.

destImg = cv2.imread('../resources/fast_mydata_20_samples_archive/cropped_sample_images_20/anon001_02350.png', cv2.IMREAD_GRAYSCALE)
srcImg = cv2.imread('../resources/fast_mydata_20_samples_archive/cropped_sample_images_20/anon001_02355.png', cv2.IMREAD_GRAYSCALE)

# \

# print(prev_img.shape)

flow = cv2.calcOpticalFlowFarneback(destImg,srcImg, None, 0.5, 3, 15, 3, 5, 1.2, 0)

padding = 200

ht, wd = destImg.shape

ww = wd + (2*padding)
hh = ht + (2*padding)

xx = (ww - wd) // 2
yy = (hh - ht) // 2

ptsA = np.zeros(flow.shape)
ptsB = np.zeros(flow.shape)

for i in range(ptsA.shape[0]):
  for j in range(ptsA.shape[1]):
    ptsA[i,j] = np.array([i,j], dtype=np.float) + np.array([padding,padding])
    ptsB[i,j] = np.array([i,j]) + (np.array(flow[i,j]))

ptsA = np.reshape(ptsA, (-1, 2))
ptsB = np.reshape(ptsB, (-1, 2))

(H, status) = cv2.findHomography(ptsB, ptsA, cv2.RANSAC, 7)

print(H)

result = cv2.warpPerspective(srcImg, H, (ww, hh))

result[yy:yy+ht, xx:xx+wd] = destImg

plt.figure(figsize=(20,10))
plt.imshow(result)

plt.show()

