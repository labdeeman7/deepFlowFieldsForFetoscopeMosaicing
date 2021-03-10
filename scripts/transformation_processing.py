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

def pointCorrespondenceWithoutPadding(flow, nonZeroI, nonZeroJ):
  """
  Obsolete code, need to remove from code base but need to be careful
  :param flow:
  :param nonZeroI:
  :param nonZeroJ:
  :return:
  """
  ptsA = np.zeros(flow.shape)
  ptsB = np.zeros(flow.shape)

  for i in range(ptsA.shape[0]):
    for j in range(ptsA.shape[1]):
      ptsA[i,j] = np.array([i,j], dtype=np.float)
      ptsB[i,j] = np.array([i,j])  +  (np.array(flow[j,i]))

  ptsA = ptsA[nonZeroI,nonZeroJ]
  ptsB = ptsB[nonZeroI,nonZeroJ]

  ptsA = np.reshape(ptsA, (-1, 2))
  ptsB = np.reshape(ptsB, (-1, 2))
  return [ptsA, ptsB]


def pointCorrespondenceWithPaddingForMiddle(flow, nonZeroI, nonZeroJ, middle_image_first, padding):
  """
  Obsolete code, needs to be removed from code base, but need to be careful
  :param flow:
  :param nonZeroI:
  :param nonZeroJ:
  :param middle_image_first:
  :param padding:
  :return:
  """

  ptsA = np.zeros(flow.shape)
  ptsB = np.zeros(flow.shape)
  if (middle_image_first) :
    for i in range(ptsA.shape[0]):
      for j in range(ptsA.shape[1]):
        ptsA[i,j] = np.array([i,j], dtype=np.float) + np.array([padding,padding])
        ptsB[i,j] = np.array([i,j])  +  (np.array(flow[j,i]))
  else:
    for i in range(ptsA.shape[0]):
      for j in range(ptsA.shape[1]):
        ptsA[i,j] = np.array([i,j], dtype=np.float)
        ptsB[i,j] = np.array([i,j])  +  (np.array(flow[j,i])) + np.array([padding,padding])

  ptsA = ptsA[nonZeroI,nonZeroJ]
  ptsB = ptsB[nonZeroI,nonZeroJ]

  ptsA = np.reshape(ptsA, (-1, 2))
  ptsB = np.reshape(ptsB, (-1, 2))
  return [ptsA, ptsB]


def getHGlobal(H_array, fullImgPaths, middle_num):
  """
    Get global H wrt a frame called middle_num. Duplicate function need to choose one. from registration processing.
    :param H_array: pair to pair transformations
    :param fullImgPaths: Image path
    :param middle_num: frame to be used as origin
    :return: returns global registration wrt to frame given by middle num.
    """
  H_global =  np.zeros((len(fullImgPaths), 3,3 ))

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