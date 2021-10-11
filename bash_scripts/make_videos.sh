#!/bin/bash

FRAME_DISTANCE=10
#400 , 300, 150, 200, 200, 200
VIDEO_NAMES=("01" "02" "10" "12")
#VIDEO_NAMES=("01" "02" "03" "05" "10" "12")
#VIDEO_NAMES=("12")
#VIDEO_NAMES=("05")


#for video_index in 0 1 2 3 4 5
for video_index in 0 1 2 3
do
    #select correct sequence
    VIDEO_NAME=${VIDEO_NAMES[video_index]}

    #create video
    cd "C:\Users\Alabi Oluwatosin\PycharmProjects\MScProject\scripts"
#    python video_processing.py --image_folder_path "C:\Users\Alabi Oluwatosin\Desktop\UCL\Modules\Project\current data\registrations_miccai\extra frames\globalRegistration_${VIDEO_NAMES[video_index]}" --video_path "C:\Users\Alabi Oluwatosin\Desktop\UCL\Modules\Project\current data\registrations_miccai\extra frames\globalRegistration_${VIDEO_NAMES[video_index]}\video.avi"
    python video_processing.py --image_folder_path "C:\Users\Alabi Oluwatosin\Desktop\UCL\Modules\Project\current data\registrations_miccai\exact\globalRegistration_${VIDEO_NAMES[video_index]}" --video_path "C:\Users\Alabi Oluwatosin\Desktop\UCL\Modules\Project\current data\registrations_miccai\exact\globalRegistration_${VIDEO_NAMES[video_index]}\video.avi"

done

