from os import listdir, mkdir
from os.path import isfile, join
import cv2

import argparse

parser = argparse.ArgumentParser(description='Just square images, why am I spending so much time on this')
parser.add_argument("--widthStart", default=80, type=int, help="Starting point of width")
parser.add_argument("--heightStart", default=80, type=int, help="starting point of height")
parser.add_argument("--squareLength", default=300, type=int, help="the square length")

args = parser.parse_args()
widthStart = args.widthStart
heightStart = args.heightStart
squareLength = args.squareLength


def crop_squares_in_image(image):
    crop_img = image[widthStart:widthStart+squareLength, heightStart:heightStart+squareLength]
    return crop_img

# def test_square_images():
#     img = cv2.imread("..\\resources\\sample_images\\anon001_02281.png")
#     crop_img = img[80:380, 80:380]
#
#     crop_img = cv2.cvtColor(crop_img,cv2.COLOR_BGR2RGB)
#
#     plt.figure(figsize=(10, 5))
#     plt.imshow(crop_img, cmap="gray")
#
#     plt.axis('off')
#     plt.show()


def make_square_images():
    # I need to get the path to each of the file and view
    # I need to
    resource_path = "C:\\Users\\Alabi Oluwatosin\\PycharmProjects\\MScProject\\resources"
    sample_image_dir_path = join(resource_path, "sample_images")
    sample_image_names = [f for f in listdir(sample_image_dir_path) if
                          isfile(join(sample_image_dir_path, f))]

    # make_directory
    cropped_image_dir_path = join(resource_path, "cropped_sample_images")
    try:
        mkdir(cropped_image_dir_path)
    except OSError as error:
        print(error)

    for image_name in sample_image_names:
        image = cv2.imread(join(sample_image_dir_path, image_name))
        cropped_image = crop_squares_in_image(image)

        cropped_image_path = join(cropped_image_dir_path, image_name)
        cv2.imwrite(cropped_image_path, cropped_image)

    print(sample_image_names[0])



make_square_images()
