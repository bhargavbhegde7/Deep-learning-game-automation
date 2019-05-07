from pathlib import Path
import os

pathlist = Path("C:/Users/Bhargav/Desktop/images/downloads/1-new").glob('**/*.*')
i = 121
for path in pathlist:
    # because path is object not string
    path_in_str = str(path)
    print(path_in_str)
    os.rename(path_in_str, str(i)+".jpg")
    i = i+1