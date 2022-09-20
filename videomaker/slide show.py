# слайд-шоу
import os
from moviepy.editor import *

directory = 'C:/Users/HOME/OneDrive/Рабочий стол/videomaker'
files = os.listdir(directory)
images = list(filter(lambda x: x.endswith('.jpg'), files))  # Ищем картинки
clips = [ImageClip(m).set_duration(2) for m in images]  # Генератор

final_clip = concatenate_videoclips([image1, image2], method='compose')  # Сшиваем
final_clip.write_videofile('slide_show.mp4', fps=24)  # Сохраняем

# Код выше позволяет делать слайд-шоу только из двух картинок. Чтобы сделать сшиваение >2, импортируем os
