import os
import shutil
path="/Users/cheng_louebrf/Desktop/python/class99"
print("before copy file:")
print(os.listdir(path))
source="/Users/cheng_louebrf/Desktop/python/class99/nedd remove.txt"
destination="/Users/cheng_louebrf/Desktop/python/class99/remove check.txt.txt"
dest=shutil.copy(source,destination)
print("after copying file:")
print(os.listdir(path))