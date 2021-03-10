import cv2
import os
import argparse
import numpy as np

parser = argparse.ArgumentParser(description='create video files from frames')
parser.add_argument("--image_folder_path", type=str, help="path to folder")
parser.add_argument("--video_path", type=str, help="path to video")
parser.add_argument("--video_frames_path", type=str, help="path to video frames")

args = parser.parse_args()
image_folder_path = args.image_folder_path
video_path = args.video_path
video_frames_path = args.video_frames_path

def generate_video(image_folder, video_name, video_frames_path):
    """
    Generate videos from warped images with lots of paddings.
    :param image_folder: folder path
    :param video_name: name for video
    :param video_frames_path: path to saved video.
    :return: none
    """
    images = [img for img in os.listdir(image_folder)
              if img.endswith(".jpg") or
              img.endswith(".jpeg") or
              img.endswith("png") or
              img.endswith("tif")]

    images.sort()

    print(images)

    frame = cv2.imread(os.path.join(image_folder, images[0]))

    height, width, layers = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter(video_name, fourcc, 1, (width, height))

    # Appending the images to the video one by one
    video_frame = np.zeros((height, width, 3), np.uint8)
    for image in images:
        img = cv2.imread(os.path.join(image_folder, image), cv2.IMREAD_UNCHANGED)
        video_frame = overlay_transparent(video_frame, img)
        cv2.imwrite(os.path.join(video_frames_path, image), video_frame)
        video.write(video_frame)

        # Deallocating memories taken for window creation
    cv2.destroyAllWindows()
    video.release()  # releasing the video generated

def overlay_transparent(bg_img, img_to_overlay_t):
    """
    Overlay new image on background only in positions where warped image is.
    :param bg_img: background image
    :param img_to_overlay_t: new image with transparent background
    :return:
    """
    # Extract the alpha mask of the RGBA image, convert to RGB
    b,g,r,a = cv2.split(img_to_overlay_t)
    overlay_color = cv2.merge((b,g,r))

    #reduce size of image
    # bg_img = get_square_in_image(bg_img)

    # Black-out the area behind the logo in our original ROI
    # img1_bg = cv2.bitwise_and(bg_img.copy(), bg_img.copy(), mask = cv2.bitwise_not(a))
    img1_bg = cv2.bitwise_and(bg_img, bg_img, mask=cv2.bitwise_not(a))

    # Mask out the logo from the logo image.
    img2_fg = cv2.bitwise_and(overlay_color, overlay_color, mask = a)

    # Update the original image with our new ROI
    bg_img = cv2.add(img1_bg, img2_fg)

    return bg_img


def get_square_in_image(image, squareLength=2000):
    """
    The padding in the image is too large, need to reduce this padding so video is very clear.
     need to change squarelength from videosequence to videosequence
    :param image: image to crop
    :param squareLength:  crop size
    :return: cropped image
    """
    h_start = int((image.shape[0] - squareLength) / 2)
    w_start = int((image.shape[1] - squareLength) / 2)

    crop_img = image[h_start:h_start + squareLength, w_start:w_start + squareLength, :, :]
    return crop_img


# Calling the generate_video function
generate_video(image_folder_path, video_path, video_frames_path)

