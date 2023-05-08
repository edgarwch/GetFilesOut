import os
from os.path import isfile, join, isdir
import shutil
import argparse

class unpacker:
    def __init__(self, sourceDir, targetDir):
        self.targetDir = targetDir
        self.path = sourceDir
        self.fileList = []
        self.file_name_list = []

    def getFiles(self):
        for r, d, f in os.walk(self.path):
            for file in f:
                self.fileList.append(os.path.join(r, file))
                self.file_name_list.append(file)
        return self.fileList
    
    def unpack(self):
        try:
            for i , file in enumerate(self.fileList):
                shutil.move(file, os.path.join(self.targetDir, self.file_name_list[i]))

            return True
        except Exception as e:
            print(e)
            return False

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--sd",
        type=str,
        nargs="?",
        default="",
        help="the source directory you want to unpack"
    )
    parser.add_argument(
        "--td",
        type=str,
        nargs="?",
        default="",
        help="the target directory you want to unpack"
    )
    opt = parser.parse_args()
    return opt

def main(opt):
    up = unpacker(opt.sd, opt.td)
    up.getFiles()
    if up.unpack():
        print("Unpack finished!")
    else:
        print("Unpack failed!")

if __name__ == "__main__":
    opt = parse_args()
    main(opt)