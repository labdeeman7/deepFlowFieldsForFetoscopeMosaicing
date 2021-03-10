#!/bin/bash

FRAME_DISTANCE=10
#400 , 300, 150, 200, 200, 200
#VIDEO_NAMES=("01" "02" "03" "05" "10" "12")
VIDEO_NAMES=("01" "02" "03" "05" "10" "12")
#VIDEO_NAMES=("05")


for video_index in 0 1 2 3 4 5
do
    #select correct sequence
    VIDEO_NAME=${VIDEO_NAMES[video_index]}

    echo "video name is " ${VIDEO_NAME}

    if [ ${VIDEO_NAME} == "01" ]
    then
       SEQ_LENGTHS=(010 020 030 040 050 060 070 080 090 100 110 120 130 140 150 160 170 180 190 200
                210 220 230 240 250 260 270 280 290 300 310 320 330 340 350 360 370 380 390 400)

    elif [ ${VIDEO_NAME} == "02" ]
    then
       SEQ_LENGTHS=(010 020 030 040 050 060 070 080 090 100 110 120 130 140 150 160 170 180 190 200
                210 220 230 240 250 260 270 280 290 300)

    elif [ ${VIDEO_NAME} == "03" ]
    then
       SEQ_LENGTHS=(010 020 030 040 050 060 070 080 090 100 110 120 130 140 150)

    elif [ ${VIDEO_NAME} == "05" ]
    then
       SEQ_LENGTHS=(010 020 030 040 050 060 070 080 090 100 110 120 130 140 150 160 170 180 190 200)
#        SEQ_LENGTHS=(010)

    elif [ ${VIDEO_NAME} == "10" ]
    then
       SEQ_LENGTHS=(010 020 030 040 050 060 070 080 090 100 110 120 130 140 150 160 170 180 190 200)

    elif [ ${VIDEO_NAME} == "12" ]
    then
       SEQ_LENGTHS=(010 020 030 040 050 060 070 080 090 100 110 120 130 140 150 160 170 180 190 200)

    else
       echo "Error None of the condition met"
       exit 125
    fi

    # perform getting merged frames
    for SEQ_LENGTH in ${SEQ_LENGTHS[@]}
    do
        echo "this is seq length"  ${SEQ_LENGTH}
        CREATE_RESPONSE_FOLDER_PATH="C:\Users\Alabi Oluwatosin\Desktop\UCL\Modules\Project\current data\registrations_miccai\extra frames\globalRegistration_${VIDEO_NAMES[video_index]}"
        OUTPUT_MERGE_FILE_PATH="C:\Users\Alabi Oluwatosin\Desktop\UCL\Modules\Project\current data\registrations_miccai\extra frames\video_frames\video_anon_0${VIDEO_NAMES[video_index]}\merge_${SEQ_LENGTH}.tif"
        RESPONSE_FILE_PATH="C:\Users\Alabi Oluwatosin\Desktop\UCL\Modules\Project\current data\registrations_miccai\extra frames\globalRegistration_${VIDEO_NAMES[video_index]}\response_file.list"

        echo ${CREATE_RESPONSE_FOLDER_PATH}
        echo ${OUTPUT_MERGE_FILE_PATH}
        echo ${RESPONSE_FILE_PATH}

        cd "C:\Users\Alabi Oluwatosin\PycharmProjects\MScProject\scripts"
        echo $PWD
        python CreateResponseFile.py --folder_path "${CREATE_RESPONSE_FOLDER_PATH}" --frame_distance ${FRAME_DISTANCE} --seq_length ${SEQ_LENGTH}

        cd "C:\Users\Alabi Oluwatosin\PycharmProjects\MScProject\applications\enblend-enfuse-4.2-win64\bin"
        echo $PWD
        ./enblend --output="${OUTPUT_MERGE_FILE_PATH}" @"${RESPONSE_FILE_PATH}"
    done

    #create video
    cd "C:\Users\Alabi Oluwatosin\PycharmProjects\MScProject\scripts"
    python video_processing.py --image_folder_path "C:\Users\Alabi Oluwatosin\Desktop\UCL\Modules\Project\current data\registrations_miccai\extra frames\video_frames\video_anon_0${VIDEO_NAMES[video_index]}" --video_path "C:\Users\Alabi Oluwatosin\Desktop\UCL\Modules\Project\current data\registrations_miccai\extra frames\video_frames\video_anon_0${VIDEO_NAMES[video_index]}\video.avi"

done

