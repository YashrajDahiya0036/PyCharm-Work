import ffmpeg
import os

# video_path = r"C:/Users/yashr/Downloads/2 Minute Timer with Music [ELECTRIC] ⚡_video.mp4"
vid_title = ""
# vid_full_path = os.path.join(video_path, vid_title)
# print(vid_full_path)



# audio_path = r"C:\Users\yashr\Downloads\2 Minute\ Timer\ with\ Music\ [ELECTRIC]\ ⚡_audio.mp4"
# audio_path = r"2 Minute Timer with Music [ELECTRIC] ⚡_audio.mp4"
nwp = "C:/Users/yashr/Downloads/v.mp4"
nap = "C:/Users/yashr/Downloads/a.mp3"
input_video = ffmpeg.input(nwp)
input_audio = ffmpeg.input(nap)
ffmpeg.concat(input_video, input_audio, v=1, a=1).output('finished_video.mp4').run()
# os.system(nap)
# os.system(nwp)
