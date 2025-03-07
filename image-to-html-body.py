from dominate import document
from dominate.tags import *
import pathlib
import picamera2
import shutil
#from psnr_test import calculate_psnr,MSE
#from comparison_mb import compare,crop
import datetime
import time
import subprocess
directory=pathlib.Path('/home/pi/Documents/mc_software')
picture_folder='/home/pi/Documents/pictures'
cap = picamera2.Picamera2()
file_name=str(datetime.datetime.now())+".png"
try:
  cap.start_and_capture_file(file_name,show_preview=False, delay=0.05)
except:
    print("Failed to capture image.")
photos = directory.glob('**/*.png')

with document(title='Pictures') as doc:
    for path in photos:
        h1(str(path))
        div(img(src=path), _class='photo')


with open('mb.html', 'w') as f:
    f.write(doc.render())



