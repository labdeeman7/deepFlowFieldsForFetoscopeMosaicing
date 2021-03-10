#!/bin/bash

VIDEO_NAME="01"
SEQ_LENGTH=400
SEQ_START=0
FRAME_DISTANCE=5

echo "this is seq length"  ${SEQ_LENGTH}
CREATE_RESPONSE_FOLDER_PATH="C:\Users\Alabi Oluwatosin\Desktop\UCL\Modules\Project\current data\registrations_mine\extra frames\globalRegistration_${VIDEO_NAME}"
OUTPUT_MERGE_FILE_PATH="C:\Users\Alabi Oluwatosin\Desktop\UCL\Modules\Project\current data\registrations_mine\extra frames\results\anon_0${VIDEO_NAME}\merge_${SEQ_LENGTH}.tif"
RESPONSE_FILE_PATH="${CREATE_RESPONSE_FOLDER_PATH}\response_file.list"



cd "C:\Users\Alabi Oluwatosin\PycharmProjects\MScProject\applications\enblend-enfuse-4.2-win64\bin"
echo $PWD
./enblend --output="${OUTPUT_MERGE_FILE_PATH}" @"${RESPONSE_FILE_PATH}"