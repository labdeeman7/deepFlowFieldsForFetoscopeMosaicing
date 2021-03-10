#!/usr/bin/python
# resize images.
from PIL import Image
import os, sys

path = "C:/Users/Alabi Oluwatosin/PycharmProjects/MScProject/resources/ambush_3_resized/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            print(item)
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((1024,384), Image.ANTIALIAS)
            imResize.save(f + '_resized.png', 'PNG', quality=90)

resize()