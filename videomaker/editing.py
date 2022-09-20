#  монтаж видео

from moviepy.editor import *

video_1 = VideoFileClip('vid1.mp4')
video_2 = VideoFileClip('vid2.mp4')

final_vid = concatenate_videoclips([video_1, video_2])  # сшиваем видео в одно

print(final_vid.duration)  # длительность конечного видео

final_vid = final_vid.subclip(2, 10)  # с каких секунд мы хотим обрезать видео

print(final_vid.duration)

final_vid = final_vid.volumex(0.2)  # уменьшаем громкость

# final_vid.write_videofile('vid3.mp4')  # тут мы его сохраняем
