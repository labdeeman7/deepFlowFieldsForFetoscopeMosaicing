# create's response files for enblend.

from os import listdir
from os.path import isfile, join
import cv2

import argparse

parser = argparse.ArgumentParser(description='create response files sequentially or 5 frames apart')
parser.add_argument("--folder_path", type=str, help="path to folder")
parser.add_argument("--frame_distance", default=10, type=int, help="response file distance between frames ")
parser.add_argument("--seq_length", type=int, help="length of sequence")
parser.add_argument("--seq_start", type=int, help="start of sequence")

args = parser.parse_args()
folder_path = args.folder_path
frame_distance = args.frame_distance
seq_length = args.seq_length
seq_start = args.seq_start


def create_response_files():
    """
    Script creates respnse files
    :return:
    """
    image_names = [f + "\n" for f in sorted(listdir(folder_path)) if isfile(join(folder_path, f)) and f.endswith(".png")]
    image_names = image_names[seq_start:seq_length + seq_start:frame_distance]

    file1 = open(join(folder_path, "response_file.list"), "w")
    file1.writelines(image_names)
    file1.close()


create_response_files()
