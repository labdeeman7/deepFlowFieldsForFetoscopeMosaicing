import cv2
import numpy as np
import matplotlib.pyplot as plt
cv2.ocl.setUseOpenCL(False)
import sys
from PIL import Image
from pathlib import Path
from os import listdir
import os
import shutil
import scripts.transformation_processing as tp


def getHGlobal(H_array, fullImgPaths, middle_num):
  """
  Get global H wrt a frame called middle_num
  :param H_array: pair to pair transformations
  :param fullImgPaths: Image path
  :param middle_num: frame to be used as origin
  :return: returns global registration wrt to frame given by middle num.
  """
  H_global = np.zeros((len(fullImgPaths), 3,3 ))

  for i in range(len(fullImgPaths)):
    # print(i)
    H_intermediate = np.eye(3)
    if i < middle_num:
      for j in range(i, middle_num):
         H_intermediate = np.matmul( H_intermediate,
                                    np.vstack([H_array[j], [0,0,1]]) )
      H_intermediate = np.linalg.inv(H_intermediate)
    elif i > middle_num:
      for j in range(middle_num, i):
         H_intermediate = np.matmul( H_intermediate,
                                    np.vstack([H_array[j], [0,0,1]]) )

    #note that if i == middle_num, we use unity array
    H_global[i] = H_intermediate

  return H_global


def globalImageRegistration(srcImg, destImg, index, mask_im, H_global, padding):
    """
    Used to perform global registration.
    Need to adjust this function, as padding no longer used.
    :param srcImg:
    :param destImg:
    :param index:
    :param mask_im:
    :param H_global:
    :param padding:
    :return:
    """
    ht, wd, cc = destImg.shape

    ww = wd + (2 * padding)
    hh = ht + (2 * padding)

    xx = (ww - wd) // 2
    yy = (hh - ht) // 2

    srcImg = cv2.bitwise_and(srcImg, srcImg, mask=mask_im)

    result = cv2.warpPerspective(srcImg, H_global[index], (ww, hh))

    return result


def globalRegistrationFirstImage(img, imageName, padding, mask_im):
    """
    depreciated code, for when I originally merged to the first image, no longer in use/
    :param img:
    :param imageName:
    :param padding:
    :param mask_im:
    :return:
    """
    ht, wd, cc = img.shape

    ww = wd + (2 * padding)
    hh = ht + (2 * padding)

    color = (0, 0, 0)
    result = np.full((hh, ww, cc), color, dtype=np.uint8)

    xx = (ww - wd) // 2
    yy = (hh - ht) // 2

    img = cv2.bitwise_and(img, img, mask=mask_im)

    result[yy:yy + ht, xx:xx + wd] = img

    return result

def getTransparentImg(src, imageName):
  """
  Get transparent images from non transparent ones
  :param src: image to be made transparent
  :param imageName: name it should be stored as
  :return: returns transparent image
  """
  tmp = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
  _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
  r, g, b = cv2.split(src)
  rgba = [b,g,r, alpha]
  dst = cv2.merge(rgba,4)
  save_name = "/content/globalRegistrationTransparent/" + imageName
  cv2.imwrite(save_name, dst)


def do_global_registration(fullImgPaths, middle_num):
    """
    obsolete code for when I merged images with the first image as origin.
    :param fullImgPaths:
    :param middle_num:
    :return:
    """
    for i in range(len(fullImgPaths) - 1):
        destImgPath = fullImgPaths[middle_num]  # the first image
        srcImgPath = fullImgPaths[i];
        srcImg, destImg = tp.inputAndVisualizeStitchPair(srcImgPath, destImgPath, False)

        imageName = Path(fullImgPaths[i]).name
        if (i == middle_num):
            src = globalRegistrationFirstImage(destImg, imageName)
        else:
            src = globalImageRegistration(srcImg, destImg, i, imageName)

        getTransparentImg(src, imageName)