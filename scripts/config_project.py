# configuration dictionary to work with video sequences.
seq_exact = {
    "anon001": {
        "name": "anon001",
        "file_length": 400,
        "start": 20,
        "v_crop_top": 0,
        "v_crop_bottom": 0,
    },
    "anon002": {
        "name": "anon002",
        "file_length": 200,
        "start": 120,
        "v_crop_top": 0,
        "v_crop_bottom": 0,
    },
    "anon003": {
        "name": "anon003",
        "file_length": 50,
        "start": 10,
        "v_crop_top": 0,
        "v_crop_bottom": 0,
    },
    "anon005": {
        "name": "anon005",
        "file_length": 100,
        "start": 20,
        "v_crop_top": 60,
        "v_crop_bottom": 20,
    },
    "anon010": {
        "name": "anon010",
        "file_length": 100,
        "start": 70,
        "v_crop_top": 80,
        "v_crop_bottom": 70,
    },
    "anon012": {
        "name": "anon006",
        "file_length": 100,
        "start": 351,
        "v_crop_top": 80,
        "v_crop_bottom": 70,
    }
}

seq_extra = {
    "anon001": {
        "name": "anon001",
        "file_length": 400,
        "start": 20,
        "v_crop_top": 0,
        "v_crop_bottom": 0,
    },
    "anon002": {
        "name": "anon002",
        "file_length": 300,
        "start": 120,
        "v_crop_top": 0,
        "v_crop_bottom": 0,
    },
    "anon003": {
        "name": "anon003",
        "file_length": 150,
        "start": 10,
        "v_crop_top": 0,
        "v_crop_bottom": 0,
    },
    "anon005": {
        "name": "anon005",
        "file_length": 200,
        "start": 20,
        "v_crop_top": 60,
        "v_crop_bottom": 20,
    },
    "anon010": {
        "name": "anon010",
        "file_length": 200,
        "start": 70,
        "v_crop_top": 80,
        "v_crop_bottom": 70,
    },
    "anon012": {
        "name": "anon012",
        "file_length": 200,
        "start": 351,
        "v_crop_top": 80,
        "v_crop_bottom": 70,
    }
}


def get_img_paths(img_paths, seq_name, is_exact):
    """
    Selecting image parts for a particular sequence, sequence can be exact amount of images, or 100 frames more
    :param img_paths: sorted sequence of image paths in anon_X folder
    :param seq_name: the name of the sequence.
    :param is_exact: whether we want to use the same amount of frames released to public or use 100 frames more
    :return: returns path of images to be used in further processing.
    """
    if is_exact:
        seq = seq_exact
    else:
        seq = seq_extra

    start = seq[seq_name]["start"]
    file_length = seq[seq_name]["file_length"]
    img_paths = img_paths[start: start + file_length]

    return img_paths


