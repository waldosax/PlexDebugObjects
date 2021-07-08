import os

def Scan(path: str, files: [], mediaList: [], subdirs: []):
    """"""
    for i in range(len(files)-1,-1,-1):
        (file, extension) = os.path.splitext(files[i])
        if (extension.lower() in [".mp4", ".mkv", ".avi", ".mov"]) == False:
            files.pop(i)
