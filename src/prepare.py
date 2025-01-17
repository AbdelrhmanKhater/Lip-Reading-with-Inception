
import os
import glob
import subprocess
import sys

'''
This script prepare training folder and its dataset for each speaker.
- Folder s{i}/datasets/train would contain original DATASET_VIDEO - s{i} with 0 <= i < VAL_SAMPLES
- Folder s{i}/datasets/val would contain s{i} >= VAL_SAMPLES
- Folder s{i}/datasets/align would contain all your *.align

Usage: 
$ python prepare.py [Path to video dataset] [Path to align dataset] [Number of samples]

Notes:
- [Path to video dataset] should be a folder with structure: /s{i}/[video]
- [Path to align dataset] should be a folder with structure: /[align].align
- [Number of samples] should be less than or equal to min(len(ls '/s{i}/*'))
'''

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

DATASET_VIDEO_PATH = sys.argv[1]
DATASET_ALIGN_PATH = sys.argv[2]

VAL_SAMPLES = int(sys.argv[3])
print(glob.glob(os.path.join(DATASET_VIDEO_PATH, '*')))

speaker_path = glob.glob(os.path.join(DATASET_VIDEO_PATH, '*'))[0]
speaker_id = os.path.splitext(speaker_path)[0].split('/')[-1]   
for s_path in glob.glob(os.path.join(DATASET_VIDEO_PATH, '*')):
    s_id = os.path.splitext(s_path)[0].split('/')[-1]
    subprocess.check_output("mkdir -p '{}'".format(os.path.join(CURRENT_PATH, speaker_id, 'datasets', 'train', s_id)), shell=True)
    print("mkdir -p '{}'".format(os.path.join(CURRENT_PATH, speaker_id, 'datasets', 'train', s_id)))
    subprocess.check_output("mkdir -p '{}'".format(os.path.join(CURRENT_PATH, speaker_id, 'datasets', 'val', s_id)), shell=True)
    print("mkdir -p '{}'".format(os.path.join(CURRENT_PATH, speaker_id, 'datasets', 'val', s_id)))
    n = 0
    for video_path in glob.glob(os.path.join(DATASET_VIDEO_PATH, s_id, '*')):
        video_id = os.path.splitext(video_path)[0].split('/')[-1]
        if n < VAL_SAMPLES:
            subprocess.check_output("cp -r '{}' '{}'".format(video_path, os.path.join(CURRENT_PATH, speaker_id, 'datasets', 'val', s_id, video_id)), shell=True)
            print("cp -r '{}' '{}'".format(video_path, os.path.join(CURRENT_PATH, speaker_id, 'datasets', 'val', s_id, video_id)))
        else:
            subprocess.check_output("cp -r '{}' '{}'".format(video_path, os.path.join(CURRENT_PATH, speaker_id, 'datasets', 'train', s_id, video_id)), shell=True)
            print("cp -r '{}' '{}'".format(video_path, os.path.join(CURRENT_PATH, speaker_id, 'datasets', 'train', s_id, video_id)))
        n += 1
      
subprocess.check_output("cp -r '{}' '{}'".format(DATASET_ALIGN_PATH, os.path.join(CURRENT_PATH, speaker_id, 'datasets', 'align')), shell=True)
