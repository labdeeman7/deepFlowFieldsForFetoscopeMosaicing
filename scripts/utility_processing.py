#utility functions.

import cv2
import numpy as np
import matplotlib.pyplot as plt
cv2.ocl.setUseOpenCL(False)
from PIL import Image
import os



def resize_all_images(current_img_path, resized_img_path, IMG_SHAPE_STANDARD):
  dirs = os.listdir(current_img_path)
  for item in dirs:
      if item.lower().endswith(('.png', '.jpg', '.jpeg')):
        im = Image.open(os.path.join(current_img_path,item))
        imResize = im.resize(IMG_SHAPE_STANDARD, Image.ANTIALIAS)
        imResize.save(os.path.join(resized_img_path,item), 'PNG')