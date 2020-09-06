import os
from moviepy.editor import VideoFileClip , concatenate_videoclips

d_path = os.path.dirname(os.path.abspath(__file__)) + "\\destination\\"

videofiles1 =[n for n in os.listdir("E:\data_augmentation\source\g1")]
videofiles2 =[n for n in os.listdir("E:\data_augmentation\source\g2")]
videofiles3 =[n for n in os.listdir("E:\data_augmentation\source\g3")]

ix = 0

for i in videofiles1:
    for j in videofiles2:
        for k in videofiles3:
            clip1 = VideoFileClip("E:\\data_augmentation\\source\\g1\\" + i)
            clip2 = VideoFileClip("E:\\data_augmentation\\source\\g2\\" +j)
            clip3 = VideoFileClip("E:\\data_augmentation\\source\\g3\\" +k)
            final_clip = concatenate_videoclips([clip1,clip2,clip3])
            final_clip.write_videofile(d_path + str(ix) + ".mp4")
            ix += 1

#clip1 = VideoFileClip("bbaf2n.mpg")
#clip2 = VideoFileClip("brbk7n.mpg")
#clip3 = VideoFileClip("lbax4n.mpg")
#final_clip = concatenate_videoclips([clip1,clip2,clip3])
#final_clip.write_videofile("1.mp4")