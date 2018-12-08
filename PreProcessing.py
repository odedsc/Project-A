import os
from shutil import copyfile
import scipy.io as sio

path = './Mat_Files '

new_dir = './Filtered_Mat_Files'
if not os.path.exists(new_dir):
    os.makedirs(new_dir)


for root, dirs, files in os.walk(path):
    for filename in files
        pulse = filename.split('pulse_')
        if pulse[1].startswith('_'):
            continue
        elif float(pulse[1])>150 or float(pulse[1])<50:
                continue
        sys = filename.split('sys_')
        if sys[1].startswith('_'):
            continue
        elif float(sys[1])>200 or float(sys[1])<50:
                continue
        dias = filename.split('dias_')
        if dias[1].startswith('_'):
            continue
        elif float(dias[1])>150 or float(dias[1])<30:
                continue
        else:
            src = root + '/' + filename
            dst = new_dir + '/' + filename
            copyfile(src, dst)
