import cv2
import glob
import os
from functions import canned, chrome

input_path = "C:/Users/User/PycharmProjects/Projeto/dataset/*.jpg"
output_dir = "resultados"
com_chrome = os.path.join(output_dir, "com_chrome")
sem_chrome = os.path.join(output_dir, "sem_chrome")
bound_box = os.path.join(output_dir, "bound_box")
icon = "C:/Users/User/PycharmProjects/Projeto/icon/chrome.jpg"
os.makedirs(output_dir, exist_ok=True)
os.makedirs(com_chrome, exist_ok=True)
os.makedirs(sem_chrome, exist_ok=True)
os.makedirs(bound_box, exist_ok=True)

for picture in glob.glob(input_path):
  imagem = canned(picture)
  base_name = os.path.basename(picture)
  output_file = os.path.join(bound_box, base_name)
  cv2.imwrite(output_file, imagem)

for picture in glob.glob(bound_box + "/*.jpg"):
  web, loc = chrome(picture, icon)
  base_name = os.path.basename(picture)

  if loc[0].size == 0:
      new_name = "sem_chrome_" + base_name
      output_file = os.path.join(sem_chrome, new_name)
      cv2.imwrite(output_file, web)
  else:
      new_name = "com_chrome_" + base_name
      output_file = os.path.join(com_chrome, new_name)
      cv2.imwrite(output_file, web)