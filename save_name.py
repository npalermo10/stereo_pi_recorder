import os
from os.path import isfile, join
import time as t
 

class File_namer():
    def __init__(self, directory, device):
        self.file_name = ""
        self.video_directory = directory
        if not os.path.exists(self.video_directory):
            os.makedirs(self.video_directory)
        self.device = device
        
    def get_name(self):
        onlyfiles = [f for f in os.listdir(self.video_directory) if isfile(join(self.video_directory, f)) and f.split("-")[0] == t.strftime('%Y_%m_%d') and f.split("-")[1][0] == self.device]
        ints = [int(item.split("_")[3][:2]) for item in onlyfiles]
        try:
            max_int = max(ints)
        except:
            max_int = 0
        new_int = str(max_int + 1).zfill(2)
        self.file_name=(self.video_directory + t.strftime('/%Y_%m_%d-') + self.device.__str__() + "_" + new_int + ".h264")
        return self.file_name
    
# example_name = "2016_4_23-L_02.h264"