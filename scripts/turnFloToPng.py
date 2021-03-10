import flowiz as f
import glob
import numpy as np
import cv2
from os.path import join
import matplotlib.pyplot as plt
from PIL import Image

files = glob.glob('C:/Users/Alabi Oluwatosin/PycharmProjects/MScProject/resources/mask_and_full_archive'
                  '/video06_archive/flow_files_video06_full/*.flo')

for flow_file in files:
    img_array = f.convert_from_file(flow_file)
    im = Image.fromarray(img_array)
    im.save(flow_file + ".png")

